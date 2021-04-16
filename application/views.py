from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class SobreView(TemplateView):
    template_name = 'about.html'


class GenerosView(TemplateView):
    template_name = 'genre.html'

