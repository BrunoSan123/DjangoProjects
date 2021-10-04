from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from pokemons.models.models import Ginasios, Pokemon,Territorios,Treinador
from pokemons.api.serializers import GinasioSerializados, PokemonSerializado,TerritorioSerializado,treinadorSerializado
from rest_framework_simplejwt.tokens import RefreshToken


def obter_tokens_para_treinador(user):
    refresh =RefreshToken.for_user(user)

    return{
        'refresh':str(refresh),
        'access': str(refresh.access_token)
    }


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def lista_de_pokemon(request):
    if request.method =='GET':
        pokemons=Pokemon.objects.all()
        serializer=PokemonSerializado(pokemons, many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer =PokemonSerializado(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])  
def lista_de_territorio(request):
    if request.method=='GET':
        territorios =Territorios.objects.all()
        serializer = TerritorioSerializado(territorios,many=True)
        return Response(serializer.data) 

    elif request.method=='POST':
        serializer=TerritorioSerializado(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

@api_view(['GET','POST'])
def lista_de_treinador(request):
    if request.method=='GET':
        treinador = Treinador.objects.all()
        serializer=treinadorSerializado(treinador,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer =treinadorSerializado(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def ginasios(request):
    if request.method=='GET':
        ginasio =Ginasios.objects.all()
        serializer =GinasioSerializados(ginasio,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer =GinasioSerializados(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
def login_treinador(request):
    treinador = Treinador.objects.filter(nome=request.data)
    serializer =treinadorSerializado(data=request.data)
    if serializer == treinador:
        token =obter_tokens_para_treinador(treinador)
        return Response(token)



