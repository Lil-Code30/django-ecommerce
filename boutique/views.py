from django.shortcuts import render
from .models import Category, Product

def home(request):
    categories = Category.objects.all()
    
    #Recuperer 8 produits aleatoires
    random_products = Product.objects.order_by('?')[:8]

    recent_products = Product.objects.order_by('-created_at')[:8]

    context = {
        'categories': categories,
        'random_products': random_products, 
        'recent_products':recent_products
    }

    return render(request,  'home.html', context)



