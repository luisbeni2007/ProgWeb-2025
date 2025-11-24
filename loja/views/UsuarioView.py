from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Usuario
from loja.forms.UserUsuarioForm import UserUsuarioForm, UserForm

def list_usuario_view(request, id=None):
    # Resto do código
    pass


def edit_usuario_view(request):
    # Recupera o objeto Usuario ligado ao usuário logado
    usuario = get_object_or_404(Usuario, user=request.user)

    # Formulário para os dados do modelo Usuario
    usuarioForm = UserUsuarioForm(instance=usuario)

    # Formulário do próprio User do Django
    userForm = UserForm(instance=request.user)

    # Contexto enviado para o template
    context = {
        'usuarioForm': usuarioForm,
        'userForm': userForm
    }

    return render(request, 'usuario/usuario-edit.html', context=context, status=200)
