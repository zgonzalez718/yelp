from django.db import models

# Create your models here.
class Food(models.Model):
     image = models.ImageField(upload_to='images/')
     food_item = models.CharField(max_length = 100, default='DEFAULT VALUE')
     description = models.CharField(max_length = 250)
     price = models.CharField(max_length = 30, default='DEFAULT VALUE')

class Meat(models.Model):
     image = models.ImageField(upload_to='images/')
     food_item = models.CharField(max_length = 100, default='DEFAULT VALUE')
     description = models.CharField(max_length = 250)
     price = models.CharField(max_length = 30, default='DEFAULT VALUE')
