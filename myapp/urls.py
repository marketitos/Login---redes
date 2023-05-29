from unicodedata import name
from django.urls import path
from myapp import views
from .views import logout
from django.contrib.auth.views import logout_then_login
#from myapp.carrito import agregar, eliminar, limpiar, restar 

urlpatterns = [
    path('', views.signup, name="signup"),
    path('kiosco/<int:id>', views.kiosco, name='kiosco'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout_ashe, name="logout"), 
    path('agregar/<int:Cards_id>', views.agregar_producto, name="Agregar"),
    path('eliminar/<int:Cards_id>', views.eliminar_producto, name="Eliminar"),
    path('restar/<int:Cards_id>', views.restar_producto, name="Restar"),
    path('limpiar/', views.limpiar_carrito, name="Clean"),
    path('carrito/', views.carrito, name="carrito")
]