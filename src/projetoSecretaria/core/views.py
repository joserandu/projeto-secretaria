from django.shortcuts import render


def index(request):
    """
    Essa função é para reendenizar as páginas html.
    """
    return render(request, 'index.html')
