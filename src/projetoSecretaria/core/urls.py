from django.urls import path
from .views import index, login, envio_mensagens_ccb, enviar_mensagens_ccb
# Tirei a outra função (enviar_mensagens) daqui de cima

# As rotas da aplicação core ficarão aqui:
urlpatterns = [
    path('', index, name="index"),
    path('login', login),
    path('envio_mensagens_ccb/', envio_mensagens_ccb, name='envio_mensagens_ccb'),
    path('enviar_mensagens_ccb/', enviar_mensagens_ccb, name='enviar_mensagens_ccb'),
]

# 'enviar_mensagens', enviar_mensagem(),
