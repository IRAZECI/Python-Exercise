""" 
Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita 
para esquerda ou vice−versa.Por exemplo: OSSO e OVO são palíndromos. 
Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o 
exemplo de uma frase palíndroma onde os espaços foram ignorados. 
Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
"""

print("--Verificador de palíndromo--")
string = input("Insira o texto:")

string_nova = "" 
 
string_l =  list(string)

for i in string_l[::-1]:
    string_nova += i
    
if string == string_nova:
    print("--RESULTADO--")
    print(f"A palavra {string_nova} é um palíndromo de {string}.")
else:
    print("--RESULTADO--")
    print(f"A palavra {string_nova} não é um palíndromo de {string}.")