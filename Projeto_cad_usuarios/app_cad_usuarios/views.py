from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def read(request):
    return redirect('listagem_usuarios')

def usuarios(request):
    
    if request.method == 'POST':
        #Salvar as informações no banco de dados
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.email = request.POST.get('email')
        novo_usuario.telefone = request.POST.get('telefone')
        novo_usuario.save()
    
    #Exibir todos os usuarios já cadastrados em uma nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    
    #Retorna os dados para a pagina de listagem de usuarios
    return render(request, 'usuarios/usuarios.html', usuarios)

def editar(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario=id_usuario)
    return render(request, 'usuarios/editar.html', {"usuario": usuario})

def update(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario=id_usuario)
    usuario.nome = request.POST.get('nome')
    usuario.idade = request.POST.get('idade')
    usuario.email = request.POST.get('email')
    usuario.telefone = request.POST.get('telefone')
    usuario.save()
    return redirect(read)

def excluir_item(request, id_usuario):
    if request.method == 'POST':
        usuario = Usuario.objects.get(pk=id_usuario)
        usuario.delete()
        return render(request, 'usuarios/excluir.html')
    else:
        return JsonResponse({'status': 'error', 'message': 'Método inválido'})