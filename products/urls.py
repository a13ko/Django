from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path("",index_view, name="index"),
    path("create/",create_view, name="create"),
]
