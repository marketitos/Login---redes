from unicodedata import name
from django.urls import path
from myapp import views
from .views import logout
from django.contrib.auth.views import logout_then_login
#from myapp.carrito import agregar, eliminar, limpiar, restar 

urlpatterns = [
    path('', views.signup, name="signup"),
    path('kiosco/', views.kiosco, name='kiosco'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout_ashe, name="logout"), 
    path('agregar/<int:Cards_id>', views.agregarProd, name="Agregar"),
    path('eliminar/<int:Cards_id>', views.eliminarProd, name="Eliminar"),
    path('restar/<int:Cards_id>', views.restarProd, name="Restar"),
    path('limpiar/', views.clean, name="Clean")
]