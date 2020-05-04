import os
import random
from colorama import Fore,Back,Style

jogarNovamente ="s"
jogadas=0
quemJoga =2
maxJogadas=9
vitoria ="n"
velha=[
       [" "," "," "],
       [" "," "," "],
       [" "," "," "]
    ]

def tela():
    global velha
    global jogadas
    os.system("cls")
    print("    0   1   2")
    print("0:  "+velha[0][0]+ " | "+velha[0][1]+ " | "+velha[0][2])
    print("   -----------")
    print("1:  "+velha[1][0]+ " | "+velha[1][1]+ " | "+velha[1][2])
    print("   -----------")
    print("2:  "+velha[2][0]+ " | "+velha[2][1]+ " | "+velha[2][2])
    print("   -----------")
    print("jogadas: "+ Fore.GREEN + str(jogadas) + Fore.RESET)


def jogador():
    global jogadas
    global quemJoga
    global maxJogadas

    if quemJoga==2 and jogadas<maxJogadas:
       
        
            try:
                
                linha =int(input("Linha..:"))
                coluna =int(input("Coluna.."))
                 
                while velha[linha][coluna]!=" ": 
                    linha =int(input("Linha..:"))
                    coluna =int(input("Coluna.."))
                velha[linha][coluna] ="x"
                quemJoga =1
                jogadas+=1
            except:
                print("linha e ou coluna invalida")
                os.system("pause")

def cpu():
    global jogadas
    global quemJoga
    global maxJogadas

    if quemJoga==1 and jogadas<maxJogadas:
        linha =random.randrange(0,3)
        coluna = random.randrange(0,3)
        while velha[linha][coluna]!=" ":
            linha =random.randrange(0,3)
            coluna = random.randrange(0,3)
        velha[linha][coluna]="o"
        jogadas+=1
        quemJoga=2
            
                
        
def VerificarVitoria():
    global velha
    Vitoria="n"
    simbolos=["x","o"]
    for s in simbolos:
        Vitoria="n"
        #verificação de linhas
        indiceLinha=IndiceCol=0
        while indiceLinha<3:
            soma=0
            IndiceCol=0
            while IndiceCol<3:
                if(velha[indiceLinha][IndiceCol] == s):
                    soma+=1
                    IndiceCol+=1
                
            if(soma == 3):
                Vitoria=s
                break
                indiceLinha+=1
        if(Vitoria!="n"):
            break

            #verificação de colunas
        indiceLinha=IndiceCol=0
        while IndiceCol<3:
            soma=0
            indiceLinha=0
            while indiceLinha<3:
                if(velha[indiceLinha][IndiceCol] == s):
                    soma+=1
                indiceLinha+=1
                
            if(soma == 3):
                Vitoria=s
                break
            IndiceCol+=1
            if(Vitoria!="n"):
                break

            #virifica diagonais

        soma=0
        idiag=0
        while idiag<3:
            if(velha[indiag][Indiag] == s):
                soma+=1
            idiag+=1
        if(soma==3):
            vitoria=s
            break

            #diagonal 2

        soma=0
        idiag1=0
        idiag2=2
        while idiag2>=0:
            if(velha[indiag1][Indiag2] == s):
                soma+=1
                idiag1+=1
                idiag2-=1
        if(soma==3):
            vitoria=s
            break
    return Vitoria


def redefinir():


     global jogadas
     global quemJoga
     global maxJogadas
     global vitoria
     global velha
    
     jogadas=0
     quemJoga =2
     maxJogadas=9
     vitoria ="n"
     velha=[
       [" "," "," "],
       [" "," "," "],
       [" "," "," "]
        ]

    

    

while True:
    tela()
    jogador()
    cpu()
    tela()
    vitoria = VerificarVitoria()
    if(vitoria!="n")or(jogadas>=maxJogadas):
        break
    
    
