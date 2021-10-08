from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from pokemons.modelos.models import Ginasios, Pokemon,Territorios,Treinador
from pokemons.api.serializers import GinasioSerializados, PokemonSerializado,TerritorioSerializado,treinadorSerializado
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST'])
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

@api_view(['GET'])
@permission_classes({IsAuthenticated})
def lista_de_treinador(request):
    if request.method=='GET':
        treinador = Treinador.objects.all()
        serializer=treinadorSerializado(treinador,many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def cadastro_de_treinadores(request):
    if request.method=='POST':
        serializer =treinadorSerializado(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

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





