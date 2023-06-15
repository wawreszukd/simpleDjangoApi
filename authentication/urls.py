from django.urls import path
from .views import *
urlpatterns = [
    path('login/', handleLogin, name='login'),
    path('logout/', handleLogOut, name='logout'),
    path('register/', handleRegister, name='register'),
]
