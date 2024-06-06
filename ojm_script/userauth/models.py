from django.db import models
from django.contrib.auth.models import AbstractUser



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
        ('none','Not a Nigerian')
    ]

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=25, blank=True)  
    whatsapp_number = models.CharField(max_length=25, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class ElectricianProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    service_description = models.TextField()
    profile_picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    founded_date = models.DateField()
    registered = models.BooleanField(default=False)
    country = models.CharField(max_length=50, choices=WEST_AFRICAN_COUNTRIES)
    state = models.CharField(max_length=50, choices=NIGERIAN_STATES)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    terms = models.BooleanField(default=False)

    number_of_employees = models.IntegerField(default=0)
    website_url = models.URLField(max_length=200, blank=True, null=True)
    youtube_url = models.URLField(max_length=200, blank=True, null=True)
    
    prices = models.TextField(blank=True, null=True)
    qualification = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Electricians"
    def __str__(self):
        return self.business_name


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    country = models.CharField(max_length=50, choices=WEST_AFRICAN_COUNTRIES)
    state = models.CharField(max_length=50, choices=NIGERIAN_STATES)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    terms = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Customers"
    def __str__(self):
        return self.user.username
        