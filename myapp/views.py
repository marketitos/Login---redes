from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.db import IntegrityError
from .models import Cards

from myapp.carrito import carrito

# Create your views here.


def Home(request):
    return render(request,'home.html')


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
                return redirect('kiosco')
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
    return render(request, 'kiskco.html',{
        'cards': cards
    })


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

def agregarProd(request, Cards_id):
    carrito= carrito(request)
    cards = Cards.objects.get(id = Cards.id)
    carrito.agregar(Cards)
    return redirect("kiosco")

def eliminarProd(request, Cards_id):
    carrito= carrito(request)
    cards = Cards.objects.get(id = Cards.id)
    carrito.eliminar(Cards)
    return redirect("kiosco")

def clean(request, Cards_id):
    carrito= carrito(request)
    cards = Cards.objects.get(id = Cards.id)
    carrito.limpiar(Cards)
    return redirect("kiosco")

def restarProd(request, Cards_id):
    carrito= carrito(request)
    cards = Cards.objects.get(id = Cards.id)
    carrito.restar(Cards)
    return redirect("kiosco")

            
        





    
    


