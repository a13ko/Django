from django.urls import path
from .views import *
from django.contrib.auth import views

app_name = 'accounts'
urlpatterns = [
    # path("login/",login_view, name="login"),
    # path("logout/",logout_view, name="logout"),
    # path("register/",register_view, name="register"),
    # path("activate/account/<activation_code>/",activate_account_view, name="activate-account"),
    # path("activate/<slug>/",activate_account_code_view, name="activate")
]
