
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #Rota, view responsável, nomede referência
    path('',views.home, name='home'),
    path('usuarios/', views.usuarios, name= 'listagem_usuarios'),
    path('editar/<int:id_usuario>/', views.editar, name= 'editar'),
    path('update/<int:id_usuario>/', views.update, name= 'update'),
    path('excluir/<int:id_usuario>/', views.excluir_item, name= 'excluir_item'),
    path('read/', views.read, name='read'),
]
