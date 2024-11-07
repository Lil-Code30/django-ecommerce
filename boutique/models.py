from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  null=True, blank=True)
    #a verifier 
    last_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username}  {self.last_name}"
 