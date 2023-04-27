from urllib import request
from .models import Cards

class carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.carrito["carrito"]
        else:
            self.carrito = carrito

def agregar(self, Cards):
    id = str(Cards.id)
    if id not in self.carrito.keys():
        self.carrito[id]={
            "Cards_id": Cards.id,
            "titulo": Cards.titulo,
            "precio": str(Cards.price),
            "cantidad": 1,
        }
    else:
        for key, value in self.carrito.items():
            if key == id:
                value["cantidad"] = value["cantidad"] + 1
                break
    self.guardar()


def guardar(self):
    self.session["carrito"] = self.carrito
    self.session.modified = True


def eliminar(self, Cards):
    id = str(Cards.id)
    if id in self.carrito:
        del self.carrito[id]
        self.guardar()


def restar(self, Cards):
    for key, value in self.carrito.items():
        if key == str(Cards.id):
            value["cantidad"] = value["cantidad"] - 1
            if value["cantidad"] < 1:
                self.eliminar(Cards)
            break
        else:
            print("El producto no existe en el carrito")    

def limpiar(self):
    self.session["carrito"] = {}
    self.session.modified = True
