from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import IndexView, SobreView, FilmesView, ContatoView, FilmeDetalheView, RelatorioFilmesView, \
    FilmeViewSet, GeneroViewSet, SessaoViewSet, UsuarioViewSet, SalaViewSet, AssentoViewSet

router = SimpleRouter()
router.register('filmes', FilmeViewSet)
router.register('generos', GeneroViewSet)
router.register('sessoes', SessaoViewSet)
router.register('usuarios', UsuarioViewSet)
router.register('salas', SalaViewSet)
router.register('assentos', AssentoViewSet)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('filmes/', FilmesView.as_view(), name='filmes'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('filme-detalhe/<int:id>/', FilmeDetalheView.as_view(), name='filme-detalhe'),
    path('relatorio-filmes/', RelatorioFilmesView.as_view(), name='relatorio-filmes'),
]
