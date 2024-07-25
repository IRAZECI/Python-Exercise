"""Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma 
palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas 
de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a 
palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo."""

import random
import sys

with open("texto1.txt", "r") as arquivo: #Abir o arquivo texto
    conteudo = arquivo.read()

lista = conteudo.split(" ") #Dividir as palavras recebidas do arquivo texto
random.shuffle(lista) #Embaralhar palavras
palavra_escolhida = lista[0] #Escolher uma palavra aleatória

palavra_escolhida_m = list(palavra_escolhida) #Depois de transformar a palavra em lista
random.shuffle(palavra_escolhida_m) #Basta apenas usar a função shuffe novamente para embaralhar as palavras
palavra_escolhida_m_f = "".join(palavra_escolhida_m)
palavra_escolhida_f = "".join(palavra_escolhida)

conta_erro = 0

print("--JOGO DE PALAVRAS EMBARALHADAS--")
while conta_erro <= 6:
    print(f"Palavra embaralhada:{palavra_escolhida_m_f}")
    resposta = input("Qual palavra você acha que é ?:")
    
    if resposta == palavra_escolhida_f:
        print("---VOCÊ VENCEU---")
        print(f"A palavra era:{palavra_escolhida_f}")
        sys.exit(1)
        
    print("-TENTE NOVAMENTE-")
    resposta =  ""
    conta_erro += 1
else:
    print("--VOCÊ PERDEU--")
    print(f"A palavra era:{palavra_escolhida_f}")
    sys.exit(1)