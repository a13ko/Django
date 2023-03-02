from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("activate/<slug>/", account_activate_view, name="activate")

]