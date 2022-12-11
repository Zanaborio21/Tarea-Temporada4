from django.db import models
from datetime import date

# Create your models here.

class Post(models.Model):
    titulo=models.CharField(max_length=20)
    descripcion = models.TextField(blank=True,default="esta es la descripcion")
    imagen = models.ImageField(null=True,blank=True,upload_to="imagenes/",default='/imagenes/mer.jpg')
    date=models.DateField(default=date.today)
    url=models.URLField(blank=True)


    def __str__(self):
        return self.titulo

class Ipe(models.Model):
    ipe=models.CharField(max_length=20)

    def __str__(self):
        return self.ipe