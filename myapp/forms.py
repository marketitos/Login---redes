from dataclasses import fields
from django.forms import ModelForm


from models import Cards
class vender(ModelForm):
    class Meta:
        model = Cards
        fields= ['Image','Titulo','price','categoria']