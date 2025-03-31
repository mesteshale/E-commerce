from django.db import models

# Create your models here.
class Product(models.Model):
    
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')


    def __str__(self):
        return self.title
