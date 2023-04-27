from distutils.command.upload import upload
from django.db import models

# Create your models here.

## Crear un models que se llame producto con una foreign key de titulo y precio para poder hacer el carrito

#Hacer qeu las cartas no se acoplen y se pongan abajo 
#arreglar la sidebar

class Cards(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images')
    titulo = models.CharField(max_length=200)
    price = models.IntegerField()
    def _str_(self):
        return self.titulo