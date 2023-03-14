from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path("",index_view, name="index"),
    path("create/",create_view, name="create"),
    path("wish/",product_wish_view, name="wish"),
    path("basket/",product_basket_view, name="basket"),
    path("wishlist/",wishlist_view, name="wishlist"),
    path("basket-list/",basket_list_view, name="basket-list"),
    path("delete-item/",delete_item_from_basket, name="delete-item"),
]
