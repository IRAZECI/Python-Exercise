"""
Tamanho de strings. Faça um programa que leia 2 strings e 
informe o conteúdo delas seguido do seu comprimento. 
Informe também se as duas strings possuem o mesmo comprimento 
e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente. 
    
 """

string1 = input("Insira a primeira string:")
string2 = input("Insira a segunda string:")

tamanho1 = len(string1)
tamanho2 = len(string2)

tamanho_igual = ""
iguais = ""

if tamanho1 == tamanho2:
    tamanho_igual = "Iguais"
else:
    tamanho_igual = "Diferentes"
    
if string1 == string2:
    iguais = "Iguais"
else:
     iguais = "Diferentes"
    
print("_"*30)   
print(f"String 1:{string1}")
print(f"String 2:{string2}")
print("_"*30)   
print(f"Tamanho de ({string1}): {tamanho1}")
print(f"Tamanho de ({string2}): {tamanho2}")
print("_"*30) 
print(f"As duas strings são de tamanhos {tamanho_igual}.")
print(f"As duas strings possuem conteúdo {iguais}.")

