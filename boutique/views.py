from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def signin_user(request):
    return render(request, 'forms/signin.html')

def home(request):
    #Recuperer 8 produits aleatoires
    random_products = Product.objects.order_by('?')[:8]

    recent_products = Product.objects.order_by('-created_at')[:8]

    context = {
        'random_products': random_products, 
        'recent_products':recent_products
    }

    return render(request,  'home.html', context)

def magasin(request):
    #Recuperer tous les produits
    products = Product.objects.all()
    return render(request,  'magasin.html', {'products': products})

def category_products(request, slug):
    #Recuperer la categorie
    categorie = get_object_or_404(Category, slug=slug)

    #Recuperer les produits de la categorie
    products =  Product.objects.filter(category=categorie)

    context = {
        'categorie': categorie, 
        'products':products
    }

    return render(request, 'category_products.html', context)


def product_detail(request, slug, cat):
    product = get_object_or_404(Product, slug= slug, category__slug = cat)
    #
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id).order_by('?')[:5]
    context = {
        'product': product,
        'related_products': related_products
    }
    return render(request, 'product_detail.html', context)

