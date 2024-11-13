from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('magasin/', views.magasin, name='magasin'),
    path('magasin/<slug:slug>/', views.category_products, name='category_products'),
    path('magasin/<slug:cat>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('register/', views.signin_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]