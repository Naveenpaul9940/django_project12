from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key = True)
    image = models.ImageField(upload_to = 'saved_images/')
    name = models.CharField(max_length = 100)
    price = models.IntegerField()