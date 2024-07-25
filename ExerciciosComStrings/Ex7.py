"""Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário 
(incluindo espaços em branco), conte:
quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u."""

print("_"*30)
string = input("Insira uma frase:")
espaco_branco = string.count(" ")
v1 = string.count("a")
v2 = string.count("e")
v3 = string.count("i")
v4 = string.count("o")
v5 = string.count("u")
v_total = v1 + v2 + v3 + v4 + v5

print("_"*30)
print(string)
print(f"Quantidade de espaços em branco na frase:{espaco_branco}")
print(f"Quantidade de vogais na frase:{v_total}")
