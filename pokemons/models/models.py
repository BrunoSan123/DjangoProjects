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

    def __str__(self):
        return self.nome

class Territorios(models.Model):
    id=models.BigAutoField(primary_key=True)
    nome_do_territorio=models.CharField(max_length=20)
    pokemons =models.ForeignKey(Pokemon,on_delete=models.CASCADE,blank=True,default=True)
    descricao =models.CharField(max_length=200)
    imagemTerritorial =models.ImageField(upload_to=upload_de_pokemon,blank=True,null=True)

    def __str__(self):
        return self.nome_do_territorio

   


class Ginasios(models.Model):
    id=models.BigAutoField(primary_key=True)
    localizacao=models.OneToOneField(Territorios,on_delete=models.CASCADE,default=True)
    nome_do_ginasio =models.CharField(max_length=15)

    def __str__(self):
        return self.nome_do_ginasio

class Treinador(models.Model):
    id=models.BigAutoField(primary_key=True)
    nome_do_treinador=models.CharField(max_length=30)
    senha=models.CharField(max_length=255, null=True)
    pokemons_coletados =models.ForeignKey(Pokemon,on_delete=models.CASCADE,default=True)
    insignias=models.ForeignKey(Ginasios,on_delete=models.CASCADE,default=True)
    foto =models.ImageField(upload_to=upload_de_pokemon,blank=True,null=True)
    



