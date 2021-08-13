

from django.contrib import admin
from django.urls import path,include
from agenda.views import ReservasViews,UsuariosViews,CheckInViews,CheckoutViews,Limpeza
from rest_framework import routers

router =routers.DefaultRouter()
router.register(r'reservas',ReservasViews)
router.register(r'usuarios',UsuariosViews)
router.register(r'check_in',CheckInViews)
router.register(r'check_out',CheckoutViews)
router.register(r'faxina',Limpeza)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
