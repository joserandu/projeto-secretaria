from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


"""
Essa função é para reendenizar as páginas html.
"""
