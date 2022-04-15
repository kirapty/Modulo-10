from django.db import models

# Create your models here.
class Company(models.Model):
    palabra = models.CharField(max_length=50)
    significado = models.CharField(max_length=200)
    uso = models.CharField(max_length=200)
    
    


