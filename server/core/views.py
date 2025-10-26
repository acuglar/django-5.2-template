from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib import messages


def home_view(request):
    messages.debug(request, "debug")
    messages.info(request, "Nova atualização disponível.")
    messages.success(request, "Operação concluída com sucesso!")
    messages.warning(request, "Atenção: verifique os dados novamente.")
    messages.error(request, "Erro ao processar requisição.")
    
    return render(request, "pages/home.html")


@login_required
def profile_view(request):
    """Renderiza a página de perfil do usuário"""
    return render(request, "pages/profile.html")
