from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from . import forms
from .models import Cards, Categoria




from myapp.carrito import Carrito


# Mejorar css carrito - Pendiente
# Descripcion de los productos - Por si pinta hacerlo
# Editar los productos



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
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'], email = request.POST["email"])
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


def eliminar(request, Cards_id):
    prod = Cards.objects.get(id = Cards_id)
    prod.delete()
    return redirect("kiosco")

def vender(request):
    form = forms.vender
    if request.method == "POST":
        print(request.POST['categoria'])
        categoria = Categoria.objects.get(id = int(request.POST['categoria']))
        
        producto = Cards.objects.create(image = request.FILES["image"],titulo = request.POST["titulo"], price = request.POST["price"], categoria= categoria)
        producto.save()
    return render(request,'vender.html',{
        'form': form
    })


def editar_prod(request, Cards_id):
    form = forms.vender
    print(Cards_id)
    carta = None
    if request.method == "POST":

        carta = Cards.objects.get(id = Cards_id)
        print("---------------------------------------------------------------")
        print(request.POST['categoria'])
        categoria = Categoria.objects.get(id = int(request.POST['categoria']))
        carta.image = request.FILES["image"]   
        carta.nombre = request.POST["titulo"]   
        carta.price = request.POST["price"]   
        carta.categoria = categoria
        carta.save()
        return redirect('/')
    else:
        return render(request,'editar.html',{
            'form': form,
            'card': carta,
        }) 
        