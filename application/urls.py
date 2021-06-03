from django.urls import path

from .views import IndexView, SobreView, FilmesView, FilmeDetalheView, RelatorioFilmesView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('filmes/', FilmesView.as_view(), name='filmes'),
    path('filme-detalhe/<int:id>/', FilmeDetalheView.as_view(), name='filme-detalhe'),
    path('relatorio-filmes/', RelatorioFilmesView.as_view(), name='relatorio-filmes'),
]
