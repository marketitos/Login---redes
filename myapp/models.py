from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Cards(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images')
    titulo = models.CharField(max_length=200)
    price = models.IntegerField()
    def _str_(self):
        return self.titulo