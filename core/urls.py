
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('products.urls')) ,
    path('api/',include('products.api.urls')) ,
    path('api/accounts/',include('accounts.api.urls')) ,
    path('accounts/',include('accounts.urls')) ,
    path('users/',include('users.urls')) ,
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)