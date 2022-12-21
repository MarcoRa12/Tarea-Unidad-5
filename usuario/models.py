from django.db import models

# Create your models here.

class createUser(models.Model):
    Nombre = models.CharField(max_length=50)
    Contraseña =models.CharField(max_length=100)
