from django.contrib import admin

# Register your models here.

from .models import Usuario, Genero, Filme, Compra, Sala, Sessao, Assento, Ingresso


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cartaz', 'duracao', 'genero', 'trailer', 'dataEstreia')


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'usuario', 'estado', 'cidade', 'cep', 'endereco', 'valor')


@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('numero',)


@admin.register(Sessao)
class SessaoAdmin(admin.ModelAdmin):
    list_display = ('data', 'horario', 'filme', 'sala')


@admin.register(Assento)
class AssentoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'sala')


@admin.register(Ingresso)
class IngressoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'sessao', 'sala', 'assento')

