from django.urls import path
from .views import *

app_name = 'products-api'

urlpatterns = [
    path("products/", ProductListView.as_view(), name="products"),
    # path("create/", ProductCreateView.as_view(), name="create"),
    
]


















# urlpatterns = [
#     path('products/',ProductListView.as_view(),name='products'),
#     path('create/',ProductCreateView.as_view(),name='create'),
#     path('products/detail/<slug>/',ProductDetailView.as_view(),name='detail'),
#     # path('products/delete/<slug>/',ProductDeleteView.as_view(),name='delete'),
#     # path('products/update/<slug>/',ProductUpdateView.as_view(),name='update'),
# ]
