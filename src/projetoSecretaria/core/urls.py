from django.urls import path
from .views import index

# As rotas da aplicação core ficarão aqui:
urlpatterns = [
    path('', index, name="index"),
]
