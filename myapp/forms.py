from dataclasses import fields
from tkinter import Widget
from django.forms import ModelForm
from .models import Cards

class vender(ModelForm):
    class Meta:
        model = Cards
        fields= ['image','titulo','price','categoria']


