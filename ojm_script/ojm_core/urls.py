from django.urls import path 
from . import views
app_name='ojm_core'
urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('user-dashboard',views.user_dashboard,name="user_dashboard"),
    path('prof-dashboard',views.prof_dashboard,name="prof_dashboard"),
    path('all',views.all_users,name="all"),
    path('single/<int:pk>',views.single_user,name="single"),
    
    path('search',views.search_view,name="search")
    
]





