"""
Jogo de Craps. Faça um programa de implemente um jogo de Craps. 
O jogador lança um par de dados, obtendo um valor entre 2 e 12.
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. 
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e 
você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,
este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar
este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar
este Ponto novamente.
"""
import random


print("--Jogo de Craps--")
v_i = input("Digite (C) para começar:")

if v_i == "C":
   v = True
   conta = 0
else:
    v = False
    print("Até a próxima")

while v == True:
    print("Lançando seus dados...")
    numero_aleatorio = random.randint(2, 12)
    if conta == 0 and numero_aleatorio == 7 or numero_aleatorio == 11:
        print("_"*15)
        print(f"Numero foi:{numero_aleatorio}")
        print("Você é um NATURAL")
        print("PARABENS VOCÊ GANHOU")
        v = False

    if conta == 0 and numero_aleatorio == 2 or numero_aleatorio == 3 or numero_aleatorio == 12:
        print("_"*15)
        print(f"Numero foi:{numero_aleatorio}")
        print("CRAPS")
        print("VOCÊ PERDEU NOOB")
        v = False

    if conta == 0 and numero_aleatorio == 4 or numero_aleatorio == 5 or numero_aleatorio == 6 or numero_aleatorio == 8 or numero_aleatorio == 9 or numero_aleatorio == 10:
        print("_"*15)
        print(f"Numero foi:{numero_aleatorio}")
        print("PONTO")
        n_aleatorio = 0
        while n_aleatorio != 7:
            n_aleatorio = random.randint(2, 12)
            if n_aleatorio == 7:
                print("_"*15)
                print(f"Numero foi:{n_aleatorio}")
                print("Numero 7, VOCÊ PERDEU")  
                v = False      
                break   
            if n_aleatorio == numero_aleatorio:
                print("_"*15)
                print(f"Numero foi:{n_aleatorio}")
                print(f"Parabens numero igual ao seu ponto, VOCÊ GANHOU")
                v = False
                break
            else:
                print("Lançando dados novamente...")
                 
    conta += 1
    
    







