from django.contrib.auth.models import Group
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from userauth.models import User, ElectricianProfile, CustomerProfile
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.tokens import default_token_generator

from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash


from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from .forms import CustomPasswordResetForm, CustomSetPasswordForm


from .forms import ElectricianSignUpForm,CustomerSignUpForm,UpdatePicture,UpdateBusinessInfo,UpdateLocation,UpdatePrices,UpdateQualification,UserUpdateForm,UpdateCustomerPicture,UpdateCustomerLocation


def sign(request):
    return render(request, 'sign.html')

def signup(request):
    if request.method == "POST":
        form = CustomerSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account till it is confirmed
            user.save()
            customer_profile = CustomerProfile.objects.create(user=user,
                                                      profile_picture=form.cleaned_data['profile_picture'],
                                                      country=form.cleaned_data['country'],
                                                      state=form.cleaned_data['state'],
                                                      city=form.cleaned_data['city'],
                                                      address=form.cleaned_data['address'],
                                                      terms=form.cleaned_data['terms'])
            customer_profile.save()
            customers, created = Group.objects.get_or_create(name='customers')

            user.groups.add(customers)
            current_site = get_current_site(request)
            mail_subject = 'Activate your OJM account.'
            message = render_to_string('verify_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            send_mail(mail_subject, message, 'Ojm Electrical', [to_email])
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}, Your registration was successful, Please check your email to confirm your address")
            return redirect('ojm_core:index')
    else:
        form = CustomerSignUpForm()

    context = {'form': form}
    return render(request, 'signup.html', context)




def prof_signup(request):
    if request.method == "POST":
        form = ElectricianSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account till it is confirmed
            user.save()
            electrician_profile = ElectricianProfile.objects.create(user=user,
                                                      business_name=form.cleaned_data['business_name'],
                                                      service_description=form.cleaned_data['service_description'],
                                                      profile_picture=form.cleaned_data['profile_picture'],
                                                      founded_date=form.cleaned_data['founded_date'],
                                                      registered=form.cleaned_data['registered'],
                                                      country=form.cleaned_data['country'],
                                                      state=form.cleaned_data['state'],
                                                      city=form.cleaned_data['city'],
                                                      address=form.cleaned_data['address'],
                                                      terms=form.cleaned_data['terms'])
            electrician_profile.save()
            electricians, created = Group.objects.get_or_create(name='electricians')

            user.groups.add(electricians)
            current_site = get_current_site(request)
            mail_subject = 'Activate your OJM account.'
            message = render_to_string('verify_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            send_mail(mail_subject, message, 'Ojm Electrical', [to_email])
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}, Your registration was successful, Please check your email to confirm your address")
            return redirect('ojm_core:index')
    else:
        form = ElectricianSignUpForm()

    context = {'form': form}
    return render(request, 'prof-signup.html', context)



def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, f"Congratulations, Your account has been verified")
        return redirect('ojm_core:index')
    else:
        return HttpResponse('Activation link is invalid!')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('ojm_core:index')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        signed_in = request.POST.get('signed_in')
        try:
            user = User.objects.get(email=email)
        except:
            messages.warning(request, f"User with {email} does not exist")
        user = authenticate(request, email=email,password=password)

        if user is not None:
            if signed_in:
                request.session.set_expiry(36000)
            else:    
                request.session.set_expiry(900)
            login(request,user)
            messages.success(request,f"You're logged in")
            return redirect('ojm_core:index')
        else:
            messages.warning(request, "user does not exist")
    return render(request, 'login.html')

def logout_view(request):

    logout(request)
    messages.warning(request, "You logged out successfully")
    return redirect('userauth:login')



class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('userauth:password_reset_done')
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    from_email = 'Ojm Electrical'

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        context['userauth'] = self.request.build_absolute_uri('/')  # Add the site URL to the context
        super().send_mail(subject_template_name, email_template_name,
                          context, from_email, to_email, html_email_template_name)

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('userauth:password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'
    
    
    
@login_required
def update_picture(request):
    profile = get_object_or_404(ElectricianProfile, user=request.user)
    if request.method == 'POST':
        profile_pic_form = UpdatePicture(request.POST, request.FILES, instance=profile)
        if profile_pic_form.is_valid():
            profile_pic_form.save()
            messages.success(request,'Profile pic updated successfully')
            return redirect('ojm_core:dashboard')  # Redirect to the profile page or any other page
    else:
        profile_pic_form = UpdatePicture(instance=profile)
        
    context = {
        'profile_pic_form':profile_pic_form,
        'profile':profile
    }
    return render(request, 'profdash.html',context)

@login_required
def update_business_info(request):
    profile = get_object_or_404(ElectricianProfile, user=request.user)
    if request.method == 'POST':
        business_form = UpdateBusinessInfo(request.POST, instance=profile)
        if business_form.is_valid():
            business_form.save()
            messages.success(request, 'Business Info updated successfully')
            return redirect('ojm_core:dashboard')  # Redirect to the profile page or any other page
        else:
            print(business_form.errors)  # Debug: Print form errors
    else:
        business_form = UpdateBusinessInfo(instance=profile)

    context = {
        'business_form': business_form,
        'profile': profile
    }
    return render(request, 'profdash.html', context)

@login_required
def update_location(request):
    profile = get_object_or_404(ElectricianProfile, user=request.user)
    if request.method == 'POST':
        location_form = UpdateLocation(request.POST, instance=profile)
        if location_form.is_valid():
            location_form.save()
            messages.success(request, 'Location updated successfully')
            return redirect('ojm_core:dashboard')  # Redirect to the profile page or any other page
        else:
            print(location_form.errors)  # Debug: Print form errors
    else:
        location_form = UpdateLocation(instance=profile)

    context = {
        'location_form': location_form,
        'profile': profile
    }
    return render(request, 'profdash.html', context)

@login_required
def update_prices(request):
    profile = get_object_or_404(ElectricianProfile, user=request.user)
    if request.method == 'POST':
        prices_form = UpdatePrices(request.POST, instance=profile)
        if prices_form.is_valid():
            prices_form.save()
            messages.success(request, 'Prices updated successfully')
            return redirect('ojm_core:dashboard')  # Redirect to the profile page or any other page
        else:
            print(prices_form.errors)  # Debug: Print form errors
    else:
        prices_form = UpdatePrices(instance=profile)

    context = {
        'prices_form': prices_form,
        'profile': profile
    }
    return render(request, 'profdash.html', context)

@login_required
def update_qualification(request):
    profile = get_object_or_404(ElectricianProfile, user=request.user)
    if request.method == 'POST':
        qualification_form = UpdateQualification(request.POST, instance=profile)
        if qualification_form.is_valid():
            qualification_form.save()
            messages.success(request, 'Qualification updated successfully')
            return redirect('ojm_core:dashboard')  # Redirect to the profile page or any other page
        else:
            print(qualification_form.errors)  # Debug: Print form errors
    else:
        qualification_form = UpdateQualification(instance=profile)

    context = {
        'qualification_form': qualification_form,
        'profile': profile
    }
    return render(request, 'profdash.html', context)


def update_user(request):
    user = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile updated successfully')
            return redirect('ojm_core:dashboard') 
        else:
            form = UserUpdateForm(instance=user)
    
    return render(request, 'profdash.html', {'form': form})

def change_password(request):
    user = request.user
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if confirm_password != new_password:
            messages.error(request,"Passwords don't match")
            return redirect('ojm_core:dashboard') 
        if check_password(old_password,user.password):
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request,"Password changed successfully")
            return redirect('ojm_core:dashboard') 
        else:
            messages.error(request,"Old password is incorrect, try again")
            return redirect('ojm_core:dashboard') 
    return render(request, 'profdash.html')
    

# Customer Updates
def update_user(request):
    user = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile updated successfully')
            return redirect('ojm_core:dashboard') 
        else:
            form = UserUpdateForm(instance=user)
    
    return render(request, 'userdash.html', {'form': form})

@login_required
def update_customer_location(request):
    profile = get_object_or_404(CustomerProfile, user=request.user)
    if request.method == 'POST':
        location_form = UpdateCustomerLocation(request.POST, instance=profile)
        if location_form.is_valid():
            location_form.save()
            messages.success(request, 'Location updated successfully')
            return redirect('ojm_core:dashboard')  
        else:
            print(location_form.errors)  
    else:
        location_form = UpdateCustomerLocation(instance=profile)

    context = {
        'location_form': location_form,
        'profile': profile
    }
    return render(request, 'userdash.html', context)

@login_required
def update_customer_picture(request):
    profile = get_object_or_404(CustomerProfile, user=request.user)
    if request.method == 'POST':
        profile_pic_form = UpdateCustomerPicture(request.POST, request.FILES, instance=profile)
        if profile_pic_form.is_valid():
            profile_pic_form.save()
            messages.success(request,'Profile pic updated successfully')
            return redirect('ojm_core:dashboard')  # Redirect to the profile page or any other page
    else:
        profile_pic_form = UpdateCustomerPicture(instance=profile)
        
    context = {
        'profile_pic_form':profile_pic_form,
        'profile':profile
    }
    return render(request, 'userdash.html',context)
