from django.contrib import admin
from .models import Product ,CustomUsers,Cart

# Register your models here.

class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id' ,'tittle' ,'discounted_price' ,'category','product_image']

class UserModelAdmin(admin.ModelAdmin):
    list_display=['id' ,'firstName' ,'lastName' ,'Email','contact', 'address']    


class CartModelAdmin(admin.ModelAdmin):
    list_display=['id' , 'user' , 'product','quantity']

admin.site.register(Product,ProductModelAdmin)    
admin.site.register(CustomUsers,UserModelAdmin)    
admin.site.register(Cart,CartModelAdmin)    