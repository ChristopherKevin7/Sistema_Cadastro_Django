from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #Salvar as informações no banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    
    #Exibir todos os usuarios já cadastrados em uma nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    
    #Retorna os dados para a pagina de listagem de usuarios
    return render(request, 'usuarios/usuarios.html', usuarios)