from django.urls import path
from . import views

urlpatterns = [
    path('sign-up', views.RegisterUser, name='register_user'),
    path('sign-in', views.LoginUser, name='login_user'),
    path('logout', views.LogoutUser, name='logout_user')
]