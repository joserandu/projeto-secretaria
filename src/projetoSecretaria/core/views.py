from django.shortcuts import render
from .logic import Aluno

def index(request):
    """Essa função é para reendenizar as páginas html."""
    return render(request, 'index.html')
