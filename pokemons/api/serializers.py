from django.db.models import fields
from rest_framework import serializers
from pokemons.models import Pokemon, Territorios,Ginasios,Treinador

class PokemonSerializado(serializers.ModelSerializer):
    class Meta:
        model =Pokemon
        fields='__all__'

class TerritorioSerializado(serializers.ModelSerializer):
    pokemons= serializers.StringRelatedField()
    class Meta:
        model=Territorios
        fields=['id','nome','pokemons','descricao','imagemTerritorial']

class GinasioSerializados(serializers.ModelSerializer):
    localizacao =serializers.StringRelatedField()
    class Meta:
        model=Ginasios
        fields=['id','nome','localizacao']

class treinadorSerializado(serializers.ModelSerializer):
    pokemons_coletados=serializers.StringRelatedField()
    insignias=serializers.StringRelatedField()
    class Meta:
        model =Treinador
        fields=['id','nome','pokemons_coletados','insignias','foto']

