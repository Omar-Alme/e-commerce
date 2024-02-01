from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='photo/products', blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])


    def __str__(self):
        return self.product_name


class Product_optionsManager(models.Manager):
    def colour(self):
        return super(Product_optionsManager, self).filter(option_category='colour', is_active=True)
    
    def size(self):
        return super(Product_optionsManager, self).filter(option_category='size', is_active=True)



option_category_choices = (
    ('size', 'size'),
    ('colour', 'colour'),
)
    
class Product_options(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    option_category = models.CharField(max_length=200, blank=True, choices = option_category_choices)
    option_value = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = Product_optionsManager()

    def __str__(self):
        return self.option_value



    


