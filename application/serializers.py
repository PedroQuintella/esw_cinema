from rest_framework import serializers

from application.models import Usuario, Genero, Filme, Sala, Sessao, Assento


class GeneroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genero
        fields = (
            'id',
            'nome'
        )


class FilmeSerializer(serializers.ModelSerializer):
    # sessoes = SessaoSerializer(many=True, read_only=True)
    # sessoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    sessoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='sessao-detail')

    class Meta:
        model = Filme
        fields = (
            'id',
            'titulo',
            'cartaz',
            'duracao',
            'sinopse',
            'trailer',
            'dataEstreia',
            'genero',
            'sessoes'
        )


class UsuarioSerializer(serializers.ModelSerializer):

    primeiro_nome = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = (
            'id',
            'nome',
            'cpf',
            'email',
            'senha',
            'primeiro_nome'
        )

    def get_primeiro_nome(self, obj):
            return str(obj.nome).split()[0]


class SalaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sala
        fields = (
            'id',
            'numero'
        )


class SessaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sessao
        fields = (
            'id',
            'data',
            'horario',
            'filme',
            'sala'
        )


class AssentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assento
        fields = (
            'id',
            'numero',
            'sala'
        )

