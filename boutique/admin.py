from django.contrib import admin
from .models import Category, Product, Client
from django.utils.html import  format_html



@admin.register(Category)
class  CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'description',  'created_at')

@admin.register(Product)
class  ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'price',  'description', 'category', 'image_preview')

    #afficher l'image du produit
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover;"­>', obj.image.url)
        return  format_html('<p>Aucun image</p>')
    
    image_preview.short_description = 'Image Preview'
    

    



@admin.register(Client)
class  ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'username',  'first_name',  'last_name', 'email', 'phone')
