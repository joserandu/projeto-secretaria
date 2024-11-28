from django.shortcuts import render
# from .logic import main


def index(request):
    """Essa função é para reendenizar as páginas html."""
    return render(request, 'index.html')


# def enviar_mensagem():
#     return main()
