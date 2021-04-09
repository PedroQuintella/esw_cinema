from django.db import models
from stdimage.models import StdImageField
import uuid

# Create your models here.


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, unique=True, help_text='Digite sem pontos e traços.')
    email = models.EmailField('Email', unique=True)
    senha = models.CharField('Senha', max_length=30)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome


class Filme(models.Model):
    titulo = models.CharField('Título', max_length=200)
    cartaz = StdImageField('Cartaz', null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 240, 'height': 356, 'crop': True}})
    sinopse = models.TextField('Sinopse', max_length=1000)
    trailer = models.URLField('Trailer', null=True, blank=True)
    dataEstreia = models.DateField('Data de Estreia', null=True, blank=True, help_text='Use este formato: DD/MM/AAAA')

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'

    def __str__(self):
        return self.titulo


class Compra(models.Model):
    codigo = models.IntegerField('Código')
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
    cidade = models.CharField('Cidade', max_length=100)
    cep = models.CharField('CEP', max_length=8, help_text='Digite sem pontos e traços.')
    endereco = models.CharField('Endereço', max_length=200)
    valor = models.DecimalField('Valor', max_digits=6, decimal_places=2)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    def __str__(self):
        return str(self.codigo)


class Sala(models.Model):
    numero = models.IntegerField('Número')

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'

    def __str__(self):
        return str(self.numero)


class Sessao(models.Model):
    data = models.DateField('Data', help_text='Use este formato: DD/MM/AAAA')
    horario = models.TimeField('Horário', help_text='Use este formato: HH:MM')
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    sala = models.OneToOneField(Sala, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Sessão'
        verbose_name_plural = 'Sessões'

    def __str__(self):
        return f'{self.data}, {self.horario}, {self.sala}, {self.filme}'


class Assento(models.Model):
    numero = models.IntegerField('Assento')
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    STATUS = (
        ('Disponível', 'Disponível'),
        ('Indisponível', 'Indisponível'),
    )
    disponibilidade = models.CharField('Disponibilidade', max_length=100, choices=STATUS)

    class Meta:
        verbose_name = 'Assento'
        verbose_name_plural = 'Assentos'

    def __str__(self):
        return f'{self.numero} (Sala {self.sala})'


class Ingresso(models.Model):
    codigo = models.IntegerField('Código')
    compra = models.ForeignKey(Compra, on_delete=models.DO_NOTHING)
    sessao = models.ForeignKey(Sessao, null=True, on_delete=models.SET_NULL)
    sala = models.ForeignKey(Sala, null=True, on_delete=models.SET_NULL)
    assento = models.ForeignKey(Assento, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Ingresso'
        verbose_name_plural = 'Ingressos'

    def __str__(self):
        return str(self.codigo)
