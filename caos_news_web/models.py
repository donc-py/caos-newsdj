from django.db import models


class New(models.Model):
    title = models.CharField(max_length=150 ,primary_key=True)
    descripcion = models.TextField()