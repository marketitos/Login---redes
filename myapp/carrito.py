from urllib import request

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
    
    if str(Cards.id) not in self.carrito.keys():
        self.carrito[Cards.id]={
            "Cards_id": Cards.id,
            "titulo": Cards.titulo,
            "precio": str(Cards.price),
            "cantidad": 1,
        }
    else:
        for key, value in self.carrito.items():
            if key == str(Cards.id):
                value["cantidad"] = value["cantidad"] + 1
                break
    self.guardar()


def guardar(self):
    self.session["carrito"] = self.carrito
    self.session.modified = True


def eliminar(self, Cards):
    Cards_id = str(Cards.id)
    if Cards_id in self.carrito:
        del self.carrito[Cards_id]
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

