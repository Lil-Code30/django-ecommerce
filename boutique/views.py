from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Client
from django.contrib.auth.models import User
from  django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def signin_user(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone = request.POST['tel']

        #Crée un nouveau  utilisateur
        if password1  !=  password2:
            messages.warning(request, 'Les deux mots de passe ne sont pas identiques')
        elif  User.objects.filter(username=username).exists():
            messages.warning(request, 'Ce nom d\'utilisateur est déjà utilisé')
        elif  User.objects.filter(email=email).exists():
            messages.warning(request, 'Cette adresse email est déjà utilisé')
        else:
            user = User.objects.create_user(username=username, email=email, password=password1,  first_name=firstname, last_name=lastname)
            user.save()

        if not user.is_superuser:
            client = Client(user=user, phone=phone)
            client.save()

            login(request, user)
            return redirect('home')
        
    return render(request, 'forms/signin.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,  'Connexion reussie !')
            return redirect('home')
        else:
            messages.warning(request, 'Nom d\'utilisateur ou mot de passe incorrect')
            return redirect('login')
    return render(request, 'forms/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,  'Vous avez ete deconnecte')
    return redirect('home')

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

