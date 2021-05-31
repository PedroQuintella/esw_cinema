from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView
from .models import Filme, Sessao


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['filmes'] = Filme.objects.order_by('-dataEstreia')[0:4]
        context['lancamentos'] = Filme.objects.order_by('-dataEstreia')[0:6]
        context['filmesDisponiveis'] = Filme.objects.order_by('-dataEstreia').all()
        return context


class SobreView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(SobreView, self).get_context_data(**kwargs)
        context['lancamentos'] = Filme.objects.order_by('-dataEstreia')[0:6]
        return context


class FilmesView(ListView):
    template_name = 'movies.html'
    model = Filme
    paginate_by = 12
    ordering = ['dataEstreia']

    def get_queryset(self):
        return Filme.objects.order_by('-dataEstreia').all()


class FilmeDetalheView(ListView):
    template_name = 'movie-detail.html'
    model = Sessao
    paginate_by = 9
    ordering = ['data']

    def get_context_data(self, **kwargs):
        context = super(FilmeDetalheView, self).get_context_data(**kwargs)
        id = self.kwargs['id']
        context['filme'] = Filme.objects.filter(id=id).first
        context['lancamentos'] = Filme.objects.order_by('-dataEstreia')[0:6]
        return context

    def get_queryset(self):
        id = self.kwargs['id']
        return Sessao.objects.filter(filme_id=id).order_by('data')
