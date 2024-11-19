from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


"""
Essa função é para reendenizar as páginas html.
"""


def contar_alunos():
    pass


def contar_dias_aulas():
    """já está feita"""
    pass


def contar_faltas_seguidas():
    """A partir do contar_dias_aulas, vamos obter um índice, e para esse índice, contaremos dele até acharmos um x"""
    pass


def armazenar_faltantes():
    """Será criado um dicionário com Nome do aluno, numero de faltas e número de telefone"""
    pass


def enviar_mensagem():
    """Aqui será realizado o loop para o envio das mensagens"""
    pass
