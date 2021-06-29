from django.db import models
from django.contrib.auth.models import AbstractUser

class New(models.Model):
    title = models.CharField(max_length=150 ,primary_key=True)
    descripcion = models.TextField()

class User(AbstractUser):
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    email = models.EmailField('email address', unique=True)