
from django.contrib import admin
from django.db.models import base
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from pokemons.views import ginasios, lista_de_pokemon, lista_de_territorio,lista_de_treinador ,cadastro_de_treinadores
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
    path('ginasios/',ginasios),
    path('cadastro_de_treinadores/',cadastro_de_treinadores),
    path('api/token',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh',TokenRefreshView.as_view(),name='token_refresh')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
