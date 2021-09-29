from django.db import models
from django.db.models.base import Model

def upload_de_pokemon(instance,filename):
    return f"{instance.id}-{filename}"

class Pokemon(models.Model):
    id=models.BigAutoField(primary_key=True)
    nome =models.CharField(max_length=30)
    tipo =models.CharField(max_length=30)
    estagio_de_evolucao =models.IntegerField()
    elemento = models.CharField(max_length=10)
    descricao = models.CharField(max_length=200)
    imagem =models.ImageField(upload_to=upload_de_pokemon,blank=True,null=True)

class Territorios(models.Model):
    id=models.BigAutoField(primary_key=True)
    nome=models.CharField(max_length=20)
    pokemons =models.ForeignKey(Pokemon,on_delete=models.CASCADE)
    descricao =models.CharField(max_length=200)
    imagemTerritorial =models.ImageField(upload_to=upload_de_pokemon,blank=True,null=True)

class Ginasios(models.Model):
    id=models.BigAutoField(primary_key=True)
    localizacao=models.OneToOneField(Territorios,on_delete=models.CASCADE)
    nome =models.CharField(max_length=15)

class Treinador(models.Model):
    id=models.BigAutoField(primary_key=True)
    nome=models.CharField(max_length=30)
    pokemons_coletados =models.ForeignKey(Pokemon,on_delete=models.CASCADE)
    insignias=models.ForeignKey(Ginasios,on_delete=models.CASCADE)
    foto =models.ImageField(upload_to=upload_de_pokemon,blank=True,null=True)



