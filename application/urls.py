from django.urls import path

from .views import IndexView, SobreView, GenerosView, FilmeDetalheView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('generos/', GenerosView.as_view(), name='generos'),
    path('filme-detalhe/<int:id>/', FilmeDetalheView.as_view(), name='filme-detalhe')
]
