from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.Home),
    path('signup/', views.signup, name="signup"),
    path('kiosco/', views.kiosco, name='kiosco'),
    path('signin/', views.signin, name='signin')
]