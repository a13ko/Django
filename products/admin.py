from django.contrib import admin
from .models import Category,Product,ProductImage
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','parent','slug','code',) 
    search_fields = ('name','code')

admin.site.register(Category,CategoryAdmin)


class ImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)
    

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)