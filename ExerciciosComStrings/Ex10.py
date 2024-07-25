"""Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 
99 e imprima-o na tela por extenso."""
import sys
print("--NUMERO POR EXTENSO--")
numero_inserido = input("Insira qualquer numero natural até 99:")

numero_lista = list(numero_inserido)

if len(numero_lista) != 2: #Caso o numero tenha menos que duas unidades (executa)
    u = numero_lista[0]
    u = int(u)
    if u == 1:
      u_ex = "um"
    if u == 2:
      u_ex = "dois"
    if u == 3:
      u_ex = "três"
    if u == 4:
      u_ex = "quatro"
    if u == 5:
      u_ex = "cinco"
    if u == 6:
      u_ex = "seis"
    if u == 7:
     u_ex = "sete"
    if u == 8:
     u_ex = "oito"
    if u == 9:
     u_ex = "nove"
    
    print("_"*30)
    print(f"{u_ex}")
    sys.exit(0)
    
else: #Caso o numero tenha mais que duas unidades (executa)
  d = numero_lista[0]
  d = int(d)
  u = numero_lista[1]
  u = int(u)
#------------------------------------------------------------------------------------ 
print("_"*30) #Caso o numero esteja entre 10 a 19 (executa)
if d == 1 and u == 0:
    print("Dez")
    sys.exit(0)
if d == 1 and u == 1:
    print("Onze")
    sys.exit(0)
if d == 1 and u == 2:
    print("Doze")
    sys.exit(0)
if d == 1 and u == 3:
    print("Treze")
    sys.exit(0)
if d == 1 and u == 4:
    print("Quatorze")
    sys.exit(0)
if d == 1 and u == 5:
    print("Quinze")
    sys.exit(0)
if d == 1 and u == 6:
    print("Dezesseis")
    sys.exit(0)
if d == 1 and u == 7:
    print("Dezesete")
    sys.exit(0)
if d == 1 and u == 8:
    print("Dezoito")
    sys.exit(0)
if d == 1 and u == 9:
    print("Dezenove")
    sys.exit(0)
    
    
#------------------------------------------------------------------------------------    
#Caso o numero seja esteja entre 20 a 99:
if d == 2:
    d_ex = "Vinte"
if d == 3:
    d_ex = "Trinta"
if d == 4: 
    d_ex = "Quarenta"
if d == 5:
    d_ex = "Cinquenta"
if d == 6:
    d_ex = "Sessenta"
if d == 7:
    d_ex = "Setenta"
if d == 8:
    d_ex = "Oitenta"
if d == 9:
   d_ex = "Noventa"
#------------------------------------------------------------------------------------  
if u == 0:
    pass
if u == 1:
    u_ex = "um"
if u == 2:
    u_ex = "dois"
if u == 3:
    u_ex = "três"
if u == 4:
    u_ex = "quatro"
if u == 5:
    u_ex = "cinco"
if u == 6:
    u_ex = "seis"
if u == 7:
    u_ex = "sete"
if u == 8:
    u_ex = "oito"
if u == 9:
    u_ex = "nove"
#------------------------------------------------------------------------------------    
if d != 0 and u == 0:
    print(d_ex)
elif d == " " and u != 0:
    print(u_ex)
elif d > 0 and u > 0:
    print(f"{d_ex} e {u_ex}")
    



