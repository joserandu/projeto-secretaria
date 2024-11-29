from django.shortcuts import render
from .logic import main
from django.http import HttpResponse


def index(request):
    """Essa função é para reendenizar as páginas html."""
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def envio_mensagens_ccb(request):
    return render(request, 'envio_mensagens_ccb.html')


def enviar_mensagens_ccb(request):
    main()
    return HttpResponse("Mensagens enviadas com sucesso!")
