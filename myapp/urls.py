from re import template
from unicodedata import name
from django.urls import path
from myapp import views
from .views import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout_then_login , PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
#from myapp.carrito import agregar, eliminar, limpiar, restar 

urlpatterns = [
    path('', views.signup, name="signup"),
    path('kiosco/', views.kiosco, name='kiosco'),
    path('filtro/<int:id>', views.filtro, name='filtro'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout_ashe, name="logout"), 
    path('agregar/<int:Cards_id>', views.agregar_producto, name="Agregar"),
    path('eliminar/<int:Cards_id>', views.eliminar_producto, name="Eliminar"),
    path('restar/<int:Cards_id>', views.restar_producto, name="Restar"),
    path('limpiar/', views.limpiar_carrito, name="Clean"),
    path('carrito/', views.carrito, name="carrito"),
    path('Vender/', views.vender, name="vender"),
    path('eliminarProd/<int:Cards_id>', views.eliminar, name="eliminar_prod"),
    path('editarProd/<int:Cards_id>', views.refreshCard, name="editar_prod"),
    path('resetearContra/', auth_views.PasswordResetView.as_view(template_name="ResetarPssw/resetview.html"), name="password_reset"),
    path('resetear_contra_send/', auth_views.PasswordResetDoneView.as_view(template_name="ResetarPssw/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="ResetarPssw/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="ResetarPssw/password_reset_complete.html"), name="password_reset_complete"),
]