from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('magasin/', views.magasin, name='magasin'),
    path('magasin/category/product/<slug:slug>', views.product_detail, name='product_detail'),
]