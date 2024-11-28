from django.urls import path
from .views import index
# Tirei a outra função (enviar_mensagens) daqui de cima

# As rotas da aplicação core ficarão aqui:
urlpatterns = [
    path('', index, name="index"),

]

# 'enviar_mensagens', enviar_mensagem(),
