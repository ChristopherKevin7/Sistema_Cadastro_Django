
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #Rota, view responsável, nomede referência
    path('',views.home, name='home'),
    path('usuarios/', views.usuarios, name= 'listagem_usuarios')
]
