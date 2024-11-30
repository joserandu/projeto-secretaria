from django.contrib import admin

# Register your models here.
from .models import Aluno
from .logic import main
from tkinter import *

admin.site.register(Aluno)

# botao = Button(admin.site, text="Clique aqui para enviar as mensagens", main())


def executar_main(modeladmin, request):  # Tirei o paramentro  queryset
    # Chama a função personalizada do logic.py

    main()
    modeladmin.message_user(request, "Função personalizada executada com sucesso!")


"""
class SeuModeloAdmin(admin.ModelAdmin):
    actions = [acao_executar_funcao]  # Registra a ação personalizada no admin

admin.site.register(SeuModelo, SeuModeloAdmin)
"""
