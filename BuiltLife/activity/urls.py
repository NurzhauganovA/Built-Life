from django.urls import path
from . import views

urlpatterns = [
    path('create-company', views.CreateCompany, name='create_company'),
    path('create-activity', views.CreateActivity, name='create_activity'),
]