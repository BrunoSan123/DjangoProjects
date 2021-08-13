from django.db import models
import uuid

from django.db.models.deletion import CASCADE
from django.db.models.fields import BigIntegerField




class Usuarios(models.Model):
    nome = models.CharField(max_length=50)
    rg =models.IntegerField()
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=50)
    data_de_cadastro =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome



class Reservas(models.Model):
    id =models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='uniqueid',auto_created=True)
    usuario =models.OneToOneField(Usuarios,on_delete=models.CASCADE)
    dias =models.IntegerField()

    



class CheckIn(models.Model):
    id =models.BigIntegerField(primary_key=True,default=True,auto_created=True)
    usuario =models.OneToOneField(Usuarios,on_delete=models.CASCADE)
    quarto = models.IntegerField()
    servico_de_quarto = models.BooleanField(default=False)
    
    def __int__(self):
        return self.quarto

    

class CheckOut(models.Model):
    id=models.BigIntegerField(primary_key=True,default=True,auto_created=True)
    usuario =models.OneToOneField(Usuarios,on_delete=models.CASCADE)
    quarto= models.OneToOneField(CheckIn,on_delete=models.CASCADE)
    despesas =models.IntegerField()


    

class Limpeza(models.Model):
    faxina=models.BooleanField(default=False)
    quarto =models.OneToOneField(CheckIn,on_delete=models.CASCADE,primary_key=True)
    horarios =models.TimeField()

    def __bool__(self):
        return self.faxina



