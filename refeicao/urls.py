from django.urls import path
from .views import *

urlpatterns = [
    path('', CardapioView.as_view(), name="home"),
    path('refeicao/criar-cardapio',CardapioCreate.as_view(), name="criar-cardapio"),
    path('refeicao/lista-cardapio',ListaCardapio.as_view(), name="lista-cardapio"),
    path('refeicao/atualizar-cardapio/<int:pk>',CardapioUpdate.as_view(), name="atualizar-cardapio"),
    path('refeicao/deletar-cardapio/<int:pk>',CardapioDelete.as_view(), name="deletar-cardapio"),
    path('componente',ComponenteView.as_view(), name="lista-componente"),
    path('componente/criar-componente',ComponenteCreate.as_view(), name="criar-componente"),
    path('componente/atualizar-componente/<int:pk>',ComponenteUpdate.as_view(), name="atualizar-componente"),
    path('componente/deletar-componente/<int:pk>',ComponenteDelete.as_view(), name="deletar-componente"),
    path('comentario/comentario',ComentarioView.as_view(), name="comentario"),
    path('comentario/criar-comentario',ComentarioCreate.as_view(), name="criar-comentario"),
    path('sobre', Sobre.as_view(), name="sobre"),
    path('qtdrefeicao',QtdRefeicaoView.as_view(), name="qtdrefeicao"),
    path('qtdrefeicao/criar-qtdrefeicao',QtdRefeicaoCreate.as_view(), name="criar-qtdrefeicao"),
    path('qtdrefeicao/atualizar-qtdrefeicao/<int:pk>/', QtdRefeicaoUpdate.as_view(), name="atualizar-qtdrefeicao"), 
    path('qtdrefeicao/deletar-qtdrefeicao/<int:pk>',QtdRefeicaoDelete.as_view(), name="deletar-qtdrefeicao"),
]