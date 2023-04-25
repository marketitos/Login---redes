from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.signup, name="signup"),
    path('kiosco/', views.kiosco, name='kiosco'),
    path('signin/', views.signin, name='signin')
]