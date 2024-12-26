from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),
    path('profile/',views.ProfileDetail.as_view(), name="profile"),
]
