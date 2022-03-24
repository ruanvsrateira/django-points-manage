from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_page, name="index_page"),
    # Rotas de adicionar aluno
    path("add_aluno_page", views.add_aluno_page, name="add_aluno_page"),
    path('add_aluno_view', views.add_aluno_view, name="add_aluno_view"),

    # Rotas de remover aluno
    path("remover_aluno_page", views.remover_aluno_page, name='remover_aluno_page'),
    path("remover_aluno_view", views.remover_aluno_view, name="remover_aluno_view"),

    # Rotas dos pontos
    path('menos_um_ponto/<int:id>', views.menos_um_ponto, name="menos_um_ponto"),
    path('mais_um_ponto/<int:id>', views.mais_um_ponto, name="mais_um_ponto")
]