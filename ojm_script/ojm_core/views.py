from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from userauth.models import User, ElectricianProfile, CustomerProfile
from userauth.forms import ElectricianSignUpForm,CustomerSignUpForm,UpdatePicture,UpdateBusinessInfo,UpdateLocation,UpdatePrices,UpdateQualification,UserUpdateForm,UpdateCustomerLocation



def index(request):
    return render(request, 'index.html')

def dashboard(request):
    if request.user.groups.filter(name='customers').exists():
        return redirect('ojm_core:user_dashboard')
    elif request.user.groups.filter(name='electricians').exists():
        return redirect('ojm_core:prof_dashboard')
    

@login_required
def user_dashboard(request):
    profile = get_object_or_404(CustomerProfile, user=request.user)
    user = request.user
    form = UserUpdateForm(instance=user)
    location_form = UpdateCustomerLocation(instance=profile)
    
    
    context = {
        'profile': profile,
        'location_form':location_form,
        'form':form,
    }
    return render(request, 'userdash.html',context)

@login_required
def prof_dashboard(request):
    profile = get_object_or_404(ElectricianProfile, user=request.user)
    user = request.user
    profile_pic_form = UpdatePicture(instance=profile)
    business_form = UpdateBusinessInfo(instance=profile)
    location_form = UpdateLocation(instance=profile)
    prices_form = UpdatePrices(instance=profile)
    qualification_form = UpdateQualification(instance=profile)
    form = UserUpdateForm(instance=user)
    
    
    context = {
        'profile': profile,
        'profile_pic_form':profile_pic_form,
        'business_form':business_form,
        'location_form':location_form,
        'prices_form':prices_form,
        'qualification_form':qualification_form,
        'form':form,
    }
    return render(request, 'profdash.html',context)

def all_users(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request,'users.html',context)

def single_user(request, pk):
    user = get_object_or_404(User,pk=pk)
    context = {
        'user':user
    }
    return render(request,'user.html',context)



def search_view(request):
    query = request.GET.get('query', '')
    context = {
        'query': query,
    }
    if query:
        if request.user.is_authenticated:
            return render(request, 'flow1.html', context)
        else:
            return render(request, 'flow.html', context)
    else:
        return render(request, 'index.html')