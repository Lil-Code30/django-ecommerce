from django.shortcuts import render, get_object_or_404
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


def product_detail(request, slug):
    product = get_object_or_404(Product, slug= slug)
    #
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id).order_by('?')[:5]
    context = {
        'product': product,
        'related_products': related_products
    }
    return render(request, 'product_detail.html', context)