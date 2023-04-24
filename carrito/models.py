from django.db import models
from myapp.models import Cards


# Create your models here.

class carrito(models.Model):
    cartas = models.ForeignKey(Cards,null=True, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    price = models.IntegerField()
    cantidad = models.IntegerField()
