from rest_framework import viewsets
from agenda.models import Reservas,Usuarios,CheckIn,CheckOut
from agenda.serializer import ReservaSerializada,UserSerializado,CheckSerializado,CheckoutSerializado
from django.db.models import F


class UsuariosViews(viewsets.ModelViewSet):
    queryset=Usuarios.objects.all()
    serializer_class=UserSerializado


class ReservasViews(viewsets.ModelViewSet):
    queryset=Reservas.objects.all()
    serializer_class=ReservaSerializada

class CheckInViews(viewsets.ModelViewSet):
    queryset=CheckIn.objects.select_related('usuario').all()
    serializer_class=CheckSerializado
    

    


class CheckoutViews(viewsets.ModelViewSet):
    queryset=CheckOut.objects.select_related('quarto').all()
    serializer_class=CheckoutSerializado
 


