from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.Home),
    path('signup/', views.signup, name="signup"),
    path('tareas/', views.tareas, name='tareas'),
    path('signin/', views.signin, name='signin')
]