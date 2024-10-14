from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)
    description =  models.TextField()
    slug =  models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image  = models.ImageField(upload_to='upload/category')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'

class Product(models.Model):
    name =  models.CharField(max_length=100)
    slug =   models.SlugField(max_length=255, unique=True)
    price =   models.DecimalField(max_digits=10, decimal_places=2)
    description =  models.TextField()
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)
    image =  models.ImageField(upload_to='upload/product')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


        
    

class Client(models.Model):
    username = models.CharField(max_length=50, unique=True)
    first_name =  models.CharField(max_length=255)
    last_name =   models.CharField(max_length=255)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

