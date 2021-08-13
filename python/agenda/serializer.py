from django.db.models import fields
from rest_framework import serializers
from agenda.models import Usuarios,Reservas,CheckIn,CheckOut,Limpeza


class UserSerializado(serializers.ModelSerializer):
    class Meta:
        model =Usuarios
        fields=['id','nome','rg','email','senha','data_de_cadastro']

class ReservaSerializada(serializers.ModelSerializer):
    class Meta:
        model=Reservas
        fields=['usuario','dias']

class CheckSerializado(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()
    class Meta:
        model=CheckIn
        fields=['id','usuario','quarto','servico_de_quarto']


class CheckoutSerializado(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()
    quarto = serializers.IntegerField()
    class Meta:
        model=CheckOut
        fields=['id','usuario','quarto','despesas']

class faxinaSeriada(serializers.ModelSerializer):
    quarto=serializers.IntegerField()
    class Meta:
        model=Limpeza
        fields=['faxina','quarto','horarios']