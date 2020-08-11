from django.urls import path
from . import views


urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.mobile_login, name='mobile_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('verify/', views.verify, name='verify'),
]