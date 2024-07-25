"""Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em 
lugar das letras, como números por exemplo. A própria palavra leet admite muitas variações, 
como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador 
e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. 
Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma 
texto e transforme-o para a grafia leet speak."""

print("--LEET SPEAK GENERATOR--")
texto_padrao = input("Insira um texto:")

texto = list(texto_padrao)
conta = 0

for l in texto:
    if l == 'a' or l == "A":
        del texto[conta]
        texto.insert(conta, '4')
    if l == 'b' or l == "B":
        del texto[conta]
        texto.insert(conta, 'I3')
    if l == 'c' or l == "C":
        del texto[conta]
        texto.insert(conta, '[')
    if l == 'd' or l == "D":
        del texto[conta] 
        texto.insert(conta, ')')
    if l == 'e' or l == "E":
        del texto[conta] 
        texto.insert(conta, '3')
    if l == 'f' or l == "F":
        del texto[conta] 
        texto.insert(conta, '|=')
    if l == 'g' or l == "G":
        del texto[conta] 
        texto.insert(conta, '6')
    if l == 'h' or l == "H":
        del texto[conta] 
        texto.insert(conta, '#')
    if l == 'i' or l == "I":
        del texto[conta] 
        texto.insert(conta, '1')
    if l == 'j' or l == "J":
        del texto[conta] 
        texto.insert(conta, ',_|')
    if l == 'k' or l == "K":
        del texto[conta] 
        texto.insert(conta, '>|')
    if l == 'l' or l == "L":
        del texto[conta] 
        texto.insert(conta, '1')
    if l == 'm' or l == "M":
        del texto[conta] 
        texto.insert(conta, '/\/\'')
    if l == 'n' or l == "N":
        del texto[conta] 
        texto.insert(conta, '^/')
    if l == 'o' or l == "O":
        del texto[conta] 
        texto.insert(conta, '0')    
    if l == 'p' or l == "P":
        del texto[conta] 
        texto.insert(conta, '|*')
    if l == 'q' or l == "Q":
        del texto[conta] 
        texto.insert(conta, '(_,)')
    if l == 'R' or l == "r":
        del texto[conta] 
        texto.insert(conta, 'I2') 
    if l == 's' or l == "S":
        del texto[conta] 
        texto.insert(conta, '5') 
    if l == 't' or l == "T":
        del texto[conta] 
        texto.insert(conta, '7')     
    if l == 'u' or l == "U":
        del texto[conta] 
        texto.insert(conta, '(_)')
    if l == 'v' or l == "V":
        del texto[conta] 
        texto.insert(conta, '\/')
    if l == 'w' or l == "W":
        del texto[conta] 
        texto.insert(conta, '\/\/')
    if l == 'x' or l == "X":
        del texto[conta] 
        texto.insert(conta, '><')
    if l == 'y' or l == "Y":
        del texto[conta] 
        texto.insert(conta, 'j')
    if l == 'z' or l == "Z":
        del texto[conta] 
        texto.insert(conta, '2')
   
    conta += 1
    
texto_f = ''.join(texto)

print("--Texto transformado para a grafia leet speak--")
print(texto_f)