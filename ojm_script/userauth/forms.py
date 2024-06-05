from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ElectricianProfile, CustomerProfile
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


WEST_AFRICAN_COUNTRIES = [
        ('nigeria', 'Nigeria'),
        ('benin', 'Benin'),
        ('burkina-faso', 'Burkina Faso'),
        ('cape-verde', 'Cape Verde'),
        ('cote-divoire', 'Côte d\'Ivoire (Ivory Coast)'),
        ('gambia', 'Gambia'),
        ('ghana', 'Ghana'),
        ('guinea', 'Guinea'),
        ('guinea-bissau', 'Guinea-Bissau'),
        ('liberia', 'Liberia'),
        ('mali', 'Mali'),
        ('mauritania', 'Mauritania'),
        ('niger', 'Niger'),
        ('senegal', 'Senegal'),
        ('sierra-leone', 'Sierra Leone'),
        ('togo', 'Togo'),
    ]

NIGERIAN_STATES = [
        ('abia', 'Abia'),
        ('adamawa', 'Adamawa'),
        ('akwa-ibom', 'Akwa Ibom'),
        ('anambra', 'Anambra'),
        ('bauchi', 'Bauchi'),
        ('bayelsa', 'Bayelsa'),
        ('benue', 'Benue'),
        ('borno', 'Borno'),
        ('cross-river', 'Cross River'),
        ('delta', 'Delta'),
        ('ebonyi', 'Ebonyi'),
        ('edo', 'Edo'),
        ('ekiti', 'Ekiti'),
        ('enugu', 'Enugu'),
        ('gombe', 'Gombe'),
        ('imo', 'Imo'),
        ('jigawa', 'Jigawa'),
        ('kaduna', 'Kaduna'),
        ('kano', 'Kano'),
        ('katsina', 'Katsina'),
        ('kebbi', 'Kebbi'),
        ('kogi', 'Kogi'),
        ('kwara', 'Kwara'),
        ('lagos', 'Lagos'),
        ('nasarawa', 'Nasarawa'),
        ('niger', 'Niger'),
        ('ogun', 'Ogun'),
        ('ondo', 'Ondo'),
        ('osun', 'Osun'),
        ('oyo', 'Oyo'),
        ('plateau', 'Plateau'),
        ('rivers', 'Rivers'),
        ('sokoto', 'Sokoto'),
        ('taraba', 'Taraba'),
        ('yobe', 'Yobe'),
        ('zamfara', 'Zamfara'),
        ('fct', 'Federal Capital Territory (FCT)'),
    ]
class ElectricianSignUpForm(UserCreationForm):
    
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Enter password', 'id': 'password'}))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'id': 'confirmPassword'}))
    business_name = forms.CharField(max_length=255, label='Business Name',widget=forms.TextInput(attrs={'placeholder': 'Business name', 'id': 'businessName'}))
    service_description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Business description, tell customers what you do in detail', 'id': 'serviceDescription','rows':4}), label='Service Description')
    profile_picture = forms.ImageField(required=False, label='Profile Image',widget=forms.FileInput(attrs={'id': 'businessProfilePicture'}))
    founded_date = forms.DateField(label='Founded Date',widget=forms.DateInput(attrs={'placeholder': 'Founded date', 'type': 'date', 'id': 'foundedDate'}))
    registered = forms.BooleanField(required=False, label='Registered Business',widget=forms.CheckboxInput(attrs={'id': 'registered'}))
    country = forms.ChoiceField(choices=WEST_AFRICAN_COUNTRIES, label='Country')
    state = forms.ChoiceField(choices=NIGERIAN_STATES, label='State')
    city = forms.CharField(max_length=255, label='City',widget=forms.TextInput(attrs={'placeholder': 'Enter city', 'id': 'city'}))
    address = forms.CharField(max_length=255, label='Address',widget=forms.TextInput(attrs={'placeholder': 'Enter address', 'id': 'address'}))
    terms = forms.BooleanField(required=True, label='I agree to the terms and conditions',widget=forms.CheckboxInput(attrs={'id': 'terms'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'phone_number','password1','password2','business_name', 'service_description', 'profile_picture', 'founded_date', 'registered', 'country', 'state', 'city', 'address', 'terms']

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name', 'id': 'firstName'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name', 'id': 'lastName'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'id': 'userName'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email Address', 'id': 'email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number', 'id': 'phone'}),
        }
        
        
class CustomerSignUpForm(UserCreationForm):
    
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Enter password', 'id': 'password'}))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'id': 'confirmPassword'}))
    profile_picture = forms.ImageField(required=False, label='Profile Image',widget=forms.FileInput(attrs={'id': 'businessProfilePicture'}))
    country = forms.ChoiceField(choices=WEST_AFRICAN_COUNTRIES, label='Country')
    state = forms.ChoiceField(choices=NIGERIAN_STATES, label='State')
    city = forms.CharField(max_length=255, label='City',widget=forms.TextInput(attrs={'placeholder': 'Enter city', 'id': 'city'}))
    address = forms.CharField(max_length=255, label='Address',widget=forms.TextInput(attrs={'placeholder': 'Enter address', 'id': 'address'}))
    terms = forms.BooleanField(required=True, label='I agree to the terms and conditions',widget=forms.CheckboxInput(attrs={'id': 'terms'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'phone_number','password1','password2','country', 'state', 'city', 'address', 'terms']

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name', 'id': 'firstName'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name', 'id': 'lastName'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'id': 'userName'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email Address', 'id': 'email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number', 'id': 'phone'}),
        }
        
    
    
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter email-address'}))

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Enter New password'}))
    new_password2 = forms.CharField(label='Confirm new password', widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirm password'}))
    

class UpdateBusinessInfo(forms.ModelForm):
    business_name = forms.CharField(max_length=255, label='Business Name',widget=forms.TextInput(attrs={'placeholder': '', 'id': 'displayName'}))
    service_description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Business description, tell customers what you do in detail', 'id': 'serviceDescription','rows':4}), label='Service Description')
    registered = forms.BooleanField(required=False, label='Registered Business',widget=forms.CheckboxInput(attrs={'id': 'registered'}))
    founded_date = forms.DateField(label='Founded Date',widget=forms.DateInput(attrs={'placeholder': 'Founded date', 'type': 'date', 'id': 'foundedDate'}))
    
    class Meta:
        model = ElectricianProfile
        fields = ['business_name','service_description','registered','founded_date','number_of_employees','website_url','youtube_url']
        
class UpdateLocation(forms.ModelForm):
    country = forms.ChoiceField(choices=WEST_AFRICAN_COUNTRIES, label='Country')
    state = forms.ChoiceField(choices=NIGERIAN_STATES, label='State')
    city = forms.CharField(max_length=255, label='City',widget=forms.TextInput(attrs={'placeholder': 'Enter city', 'id': 'city'}))
    address = forms.CharField(max_length=255, label='Address',widget=forms.TextInput(attrs={'placeholder': 'Enter address', 'id': 'address'}))
    
    class Meta:
        model = ElectricianProfile
        fields = ['country','state','city','address']
        
class UpdateCustomerLocation(forms.ModelForm):
    country = forms.ChoiceField(choices=WEST_AFRICAN_COUNTRIES, label='Country')
    state = forms.ChoiceField(choices=NIGERIAN_STATES, label='State')
    city = forms.CharField(max_length=255, label='City',widget=forms.TextInput(attrs={'placeholder': 'Enter city', 'id': 'city'}))
    address = forms.CharField(max_length=255, label='Address',widget=forms.TextInput(attrs={'placeholder': 'Enter address', 'id': 'address'}))
    
    class Meta:
        model = CustomerProfile
        fields = ['country','state','city','address']
        
class UpdatePicture(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, label='',widget=forms.FileInput(attrs={'id': 'fileInput'}))
    
    class Meta:
        model = ElectricianProfile 
        fields = ['profile_picture']
        
class UpdateCustomerPicture(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, label='',widget=forms.FileInput(attrs={'id': 'fileInput'}))
    
    class Meta:
        model = CustomerProfile 
        fields = ['profile_picture']
        
class UpdatePrices(forms.ModelForm):
    prices = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '', 'id': 'prices','rows':4}), label='Prices')
    
    class Meta:
        model = ElectricianProfile
        fields = ['prices']
        
class UpdateQualification(forms.ModelForm):
    qualification = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '', 'id': 'qualification','rows':4}), label='Prices')
    
    class Meta:
        model = ElectricianProfile
        fields = ['qualification']
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'whatsapp_number']