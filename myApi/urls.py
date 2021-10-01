"""myApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db.models import base
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from pokemons.views import lista_de_pokemon, lista_de_territorio,lista_de_treinador
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

#router= routers.DefaultRouter()
#router.register(r'pokemons/',lista_de_pokemon,basename='pokemon-list')
#router.register(r'territórios/',lista_de_territorio,basename='territorio-lista')
#router.register(r'treinadores/',lista_de_treinador,basename='treinador-lista')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokemons/',lista_de_pokemon),
    path('territorios/',lista_de_territorio),
    path('treinadores/',lista_de_treinador),
    path('api/token',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh',TokenRefreshView.as_view(),name='token_refresh')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
