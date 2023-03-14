from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("change-password/", password_change_view, name="change-password"),
    path("reset/", reset_password_view, name="reset"),
    path("reset-complete/<slug>/", reset_complete_view, name="reset-complete"),
    path("activate/<slug>/", account_activate_view, name="activate")

]