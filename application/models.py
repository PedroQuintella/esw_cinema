# Create your models here.
from django.db import models
from stdimage.models import StdImageField
import uuid
from django.utils.translation import gettext_lazy as _


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Usuario(models.Model):
    nome = models.CharField(_('Nome'), max_length=100)
    cpf = models.CharField(_('CPF'), max_length=11, unique=True, help_text=_('Digite sem pontos e traços.'))
    email = models.EmailField(_('Email'), unique=True)
    senha = models.CharField(_('Senha'), max_length=30)

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')

    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(_('Nome'), null=True, unique=True, max_length=200)

    class Meta:
        verbose_name = _('Gênero')
        verbose_name_plural = _('Gêneros')

    def __str__(self):
        return self.nome


class Filme(models.Model):
    titulo = models.CharField(_('Título'), max_length=200)
    cartaz = StdImageField(_('Cartaz'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 240, 'height': 356, 'crop': True}})
    duracao = models.CharField(_('Duração'), max_length=8, help_text=_('Use este formato: 02h30min'))
    sinopse = models.TextField(_('Sinopse'), max_length=1000)
    trailer = models.URLField(_('Trailer'), null=True, blank=True)
    dataEstreia = models.DateField(_('Data de Estreia'), null=True, blank=True, help_text=_('Use este formato: DD/MM/AAAA'))
    genero = models.ForeignKey(Genero, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _('Filme')
        verbose_name_plural = _('Filmes')

    def __str__(self):
        return self.titulo


class Compra(models.Model):
    codigo = models.IntegerField(_('Código'), unique=True)
    OPCOES = (
        ('AC', 'AC'),
        ('AL', 'AL'),
        ('AP', 'AP'),
        ('AM', 'AM'),
        ('BA', 'BA'),
        ('CE', 'CE'),
        ('DF', 'DF'),
        ('ES', 'ES'),
        ('GO', 'GO'),
        ('MA', 'MA'),
        ('MT', 'MT'),
        ('MS', 'MS'),
        ('MG', 'MG'),
        ('PA', 'PA'),
        ('PB', 'PB'),
        ('PR', 'PR'),
        ('PE', 'PE'),
        ('PI', 'PI'),
        ('RJ', 'RJ'),
        ('RN', 'RN'),
        ('RS', 'RS'),
        ('RO', 'RO'),
        ('RR', 'RR'),
        ('SC', 'SC'),
        ('SP', 'SP'),
        ('SE', 'SE'),
        ('TO', 'TO'),
    )
    estado = models.CharField('UF', max_length=100, choices=OPCOES)
    cidade = models.CharField(_('Cidade'), max_length=100)
    cep = models.CharField(_('CEP'), max_length=8, help_text=_('Digite sem pontos e traços.'))
    endereco = models.CharField(_('Endereço'), max_length=200)
    valor = models.DecimalField(_('Valor'), max_digits=6, decimal_places=2)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _('Compra')
        verbose_name_plural = _('Compras')

    def __str__(self):
        return str(self.codigo)


class Sala(models.Model):
    numero = models.IntegerField(_('Número'), unique=True)

    class Meta:
        verbose_name = _('Sala')
        verbose_name_plural = _('Salas')

    def __str__(self):
        return str(self.numero)


class Sessao(models.Model):
    data = models.DateField(_('Data'), help_text=_('Use este formato: DD/MM/AAAA'))
    horario = models.TimeField(_('Horário'), help_text=_('Use este formato: HH:MM'))
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('Sessão')
        verbose_name_plural = _('Sessões')

    def __str__(self):
        return f'{self.data}, {self.horario}, {self.sala}, {self.filme}'


class Assento(models.Model):
    numero = models.IntegerField(_('Assento'))
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    STATUS = (
        ('Disponível', _('Disponível')),
        ('Indisponível', _('Indisponível')),
    )
    disponibilidade = models.CharField(_('Disponibilidade'), max_length=100, choices=STATUS)

    class Meta:
        verbose_name = _('Assento')
        verbose_name_plural = _('Assentos')

    def __str__(self):
        return f'{self.numero} (Sala {self.sala})'


class Ingresso(models.Model):
    codigo = models.IntegerField(_('Código'), unique=True)
    compra = models.ForeignKey(Compra, on_delete=models.DO_NOTHING)
    sessao = models.ForeignKey(Sessao, null=True, on_delete=models.SET_NULL)
    sala = models.ForeignKey(Sala, null=True, on_delete=models.SET_NULL)
    assento = models.ForeignKey(Assento, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('Ingresso')
        verbose_name_plural = _('Ingressos')

    def __str__(self):
        return str(self.codigo)
