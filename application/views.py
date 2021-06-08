# Create your views here.
from django.views.generic import TemplateView, ListView, FormView
from .models import Filme, Sessao, Genero, Usuario, Assento, Sala

from django_weasyprint import WeasyTemplateView
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML

from django.utils.translation import gettext as _
from django.utils import translation

from .forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib import messages

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets

from . import serializers
from application.serializers import GeneroSerializer, FilmeSerializer, UsuarioSerializer, SalaSerializer, SessaoSerializer, AssentoSerializer


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        lang = translation.get_language()
        context['lang'] = lang
        context['filmes'] = Filme.objects.order_by('-dataEstreia')[0:4]
        context['lancamentos'] = Filme.objects.order_by('-dataEstreia')[0:6]
        context['filmesDisponiveis'] = Filme.objects.order_by('-dataEstreia').all()
        translation.activate(lang)
        return context


class SobreView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(SobreView, self).get_context_data(**kwargs)
        context['lancamentos'] = Filme.objects.order_by('-dataEstreia')[0:6]
        return context


class RelatorioFilmesView(WeasyTemplateView):

    def get(self, request, *args, **kwargs):
        filmes = Filme.objects.order_by('-dataEstreia').all()

        html_string = render_to_string('relatorio-filmes.html', {'filmes': filmes})

        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        html.write_pdf(target='/tmp/relatorio-filmes.pdf')
        fs = FileSystemStorage('/tmp')

        with fs.open('relatorio-filmes.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="relatorio-filmes.pdf"'
        return response


class FilmesView(ListView):
    template_name = 'movies.html'
    model = Filme
    paginate_by = 12
    ordering = ['dataEstreia']

    def get_queryset(self):
        return Filme.objects.order_by('-dataEstreia').all()


class ContatoView(FormView):
    template_name = 'contact.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato')

    def get_context_data(self, **kwargs):
        context = super(ContatoView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _('E-mail enviado com sucesso'), extra_tags='success')
        return super(ContatoView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Falha ao enviar e-mail'), extra_tags='danger')
        return super(ContatoView, self).form_invalid(form, *args, **kwargs)


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


class FilmeViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )

    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

    @action(detail=True, methods=['get'])
    def sessoes(self, request, pk=None):
        sessoes = Sessao.objects.filter(filme_id=pk)
        page = self.paginate_queryset(sessoes)

        if page is not None:
            serializer = SessaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = SessaoSerializer(sessoes, many=True)
        return Response(serializer.data)


class GeneroViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)

    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

    @action(detail=True, methods=['get'])
    def filmes(self, request, pk=None):
        filmes = Filme.objects.filter(genero_id=pk)
        page = self.paginate_queryset(filmes)

        if page is not None:
            serializer = FilmeSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = FilmeSerializer(filmes, many=True)
        return Response(serializer.data)


class SessaoViewSet(viewsets.ModelViewSet):
    queryset = Sessao.objects.all()
    serializer_class = SessaoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer


class AssentoViewSet(viewsets.ModelViewSet):
    queryset = Assento.objects.all()
    serializer_class = AssentoSerializer
