from urllib import request


class carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session["carrito"]
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.carrito["carrito"]
        else:
            self.carrito = carrito

def agregar(self, Cards):
    id = str(Cards.id)
    if id not in self.carrito.keys():
        self.carrito[id]={
            "Cards_id":Cards.id,
            "titulo":Cards.titulo,
            "precio":Cards.precio,
            "cantidad":1,
        }
    else:
        self.carrito[id]["cantidad"] +=1,
        self.carrito[id]["precio"] += Cards.precio
