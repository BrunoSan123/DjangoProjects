from rest_framework import viewsets
from agenda.models import Reservas,Usuarios,CheckIn,CheckOut,Limpeza
from agenda.serializer import ReservaSerializada,UserSerializado,CheckSerializado,CheckoutSerializado,faxinaSeriada
from django.db.models import F


class UsuariosViews(viewsets.ModelViewSet):
    queryset=Usuarios.objects.all()
    serializer_class=UserSerializado


class ReservasViews(viewsets.ModelViewSet):
    queryset=Reservas.objects.all()
    serializer_class=ReservaSerializada

class CheckInViews(viewsets.ModelViewSet):
    queryset=CheckIn.objects.select_related('usuario')
    serializer_class=CheckSerializado
    

    


class CheckoutViews(viewsets.ModelViewSet):
    queryset=CheckOut.objects.select_related('quarto','usuario')
    serializer_class=CheckoutSerializado

class Limpeza(viewsets.ModelViewSet):
    queryset=Limpeza.objects.select_related('quarto')
    serializer_class=faxinaSeriada
 


