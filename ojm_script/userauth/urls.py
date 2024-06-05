from django.urls import path 
from . import views
from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

app_name='userauth'
urlpatterns = [
    path('sign', views.sign, name="sign"),
    path('signup', views.signup, name="signup"),
    path('prof-signup', views.prof_signup, name="prof-signup"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    
    
    path('update-pic', views.update_picture, name="update_pic"),
    path('update-customer-pic', views.update_customer_picture, name="update_customer_pic"),
    path('update-business-info',views.update_business_info,name="business_info"),
    path('update-location',views.update_location,name="location"),
    path('update-customer-location',views.update_customer_location,name="customer_location"),
    path('update-prices',views.update_prices,name="prices"),
    path('update-qualification',views.update_qualification,name="qualification"),
    path('update-user',views.update_user,name="update_user"),
    path('change-password',views.change_password,name="change_password"),
    
    
    
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
