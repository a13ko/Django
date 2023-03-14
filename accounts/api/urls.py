from django.urls import path
from .views import *

app_name = 'accounts-api'

urlpatterns = [
    path("login/", loginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("activate/<slug>/", ActivationView.as_view(), name="activate"),
    
]
