from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from . import forms
from .models import Cards, Categoria



from myapp.carrito import Carrito

# Create your views here.
# Crear vista para vender productos
# Cambiar contraseña
# Mejorar css carrito
# Descripcion de los productos


def Home(request):
    return render(request,'home.html')


def vender(request):
    return render(request, 'vender.html')




def signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html',{
            "form":UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('signin')
            except IntegrityError:
                return render(request, 'signup.html',{
                "form":UserCreationForm,
                "error":'El Usuario Ya Existe'
                })

        return render(request, 'signup.html',{
            "form":UserCreationForm,
            "error": 'Las contraseñas no coinciden'
            })
    
def kiosco(request):


    cards = Cards.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'kiskco.html',{
        'cards': cards,
        'categorias': categorias
    })

def filtro(request, id):
    categorias = Categoria.objects.all()
    cards = Cards.objects.all().filter(categoria_id = id)
    return render(request, 'kiskco.html',{
        'cards': cards,
        'categorias': categorias
    })

def carrito(request):
    return render(request, 'carrito.html')


def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html',{
        "form": AuthenticationForm
        })
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])

        if user is None:
            return render(request,'signin.html',{
                "form": AuthenticationForm,
                "error": "El usuario o la contraseña son incorrectos"
             })
        else:
            login(request, user)
            return redirect('kiosco')

def logout_ashe(request):
    logout(request)
    return redirect('signin')



def agregar_producto(request, Cards_id):
    carrito = Carrito(request)
    card = Cards.objects.get(id=Cards_id)
    carrito.agregar(card)
    return redirect("kiosco")

def eliminar_producto(request, Cards_id):
    carrito = Carrito(request)
    card = Cards.objects.get(id=Cards_id)
    carrito.eliminar(card)
    return redirect("kiosco")

def restar_producto(request, Cards_id):
    carrito = Carrito(request)
    card = Cards.objects.get(id=Cards_id)
    carrito.restar(card)
    return redirect("kiosco")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("kiosco")

def vender(request):
    form = forms.vender
    if request.method == "POST":
        print(request.POST)
    return render(request,'vender.html',{
        'form': form
    })