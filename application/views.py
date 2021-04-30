from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
from .models import Filme


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


class GenerosView(TemplateView):
    template_name = 'genre.html'

    def get_context_data(self, **kwargs):
        context = super(GenerosView, self).get_context_data(**kwargs)
        context['filmesDisponiveis'] = Filme.objects.order_by('-dataEstreia').all()
        return context

