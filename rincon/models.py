from django.db import models

# Create your models here.
class Food(models.Model):
     image = models.ImageField(upload_to='images/')
     description = models.CharField(max_length = 250)
