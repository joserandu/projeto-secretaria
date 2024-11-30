from django.shortcuts import render
from .logic import main
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required


def index(request):
    """Essa função é para reendenizar as páginas html."""
    return render(request, 'index.html')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)

            return render(request, 'envio_mensagens_ccb.html')
        else:
            return HttpResponse("Email ou senha inválidos")


@login_required(login_url="/login")
def envio_mensagens_ccb(request):
    return render(request, 'envio_mensagens_ccb.html')


# Sem o decorator:   if request.user.is_althenticated:
@login_required(login_url="/login")
def enviar_mensagens_ccb(request):
    main()
    return HttpResponse("Mensagens enviadas com sucesso!")
