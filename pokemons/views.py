from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from pokemons.models.models import Pokemon,Territorios,Treinador
from pokemons.api.serializers import PokemonSerializado,TerritorioSerializado,treinadorSerializado


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



