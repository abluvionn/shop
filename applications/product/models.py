from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class category(models.Model):
    slug = models.SlugField(max_length=30,primary_key=True)
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.slug
class Product(models.Model):
    owner = models.ForeignKey(User, related_name='products', on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(category, related_name='products', on_delete = models.CASCADE)
    image = models.ImageField(upload_to='images',null=True,blank=True)

    def __str__(self):
        return self.name
