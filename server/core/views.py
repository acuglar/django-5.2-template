from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home_view(request):
    """Renderiza a home page"""
    return render(request, "pages/home.html")


@login_required
def profile_view(request):
    """Renderiza a página de perfil do usuário"""
    return render(request, "pages/profile.html")
