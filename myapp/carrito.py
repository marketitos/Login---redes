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
    print(Cards)
    id = str(Cards.id)
    
    if id not in self.carrito.keys():
        self.carrito[id]={
            "Cards_id":Cards.id,
            "titulo":Cards.titulo,
            "precio":Cards.precio,
            "cantidad":1,
        }
    else:
        self.carrito[id]["cantidad"] +=1
        self.carrito[id]["precio"] += Cards.precio
    self.guardar()


def guardar(self):
    self.session["carrito"] = self.carrito
    self.session.modified = True


def eliminar(self, Cards):
    id = str(Cards.id)
    if id in self.carrito:
        del self.carrito[id]


def restar(self, Cards):
    id = str(Cards.id)
    if id in self.carrito.keys():
        self.carrito[id]["cantidad"] -=1,
        self.carrito[id]["precio"] -= Cards.precio
        if self.carrito[id]["cantidad"] <= 0 : 
            self.eliminar(Cards)
            self.guardar()

def limpiar(self):
    self.session["carrito"] = {}
    self.session.modified = True

