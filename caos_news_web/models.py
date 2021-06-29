from django.db import models
from django.contrib.auth.models import AbstractUser

class New(models.Model):
    nombre = models.CharField(max_length=150 ,primary_key=True)
    noticia = models.TextField(default='email')
    email = models.CharField(max_length=50,default='email')
    documento = models.CharField(max_length=50,default='documento')
    pasaporte = models.CharField(max_length=50,default='pasaporte')
    telefono = models.CharField(max_length=50,default='telefono')
    ciudad = models.CharField(max_length=50,default='ciudad')


class User(AbstractUser):
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    email = models.EmailField('email address', unique=True)