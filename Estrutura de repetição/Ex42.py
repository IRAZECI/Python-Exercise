#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
numero = 0
conta_1 = 0
conta_2 = 0
conta_3 = 0
conta_4 = 0

while numero >= 0:
    numero = int(input("Insira um numero:"))
    if numero > 0 and numero <= 25:
        conta_1 += 1 
    elif numero > 25 and numero <= 50:
        conta_2 += 1 
    elif numero > 50 and numero <= 75:
        conta_3 += 1 
    elif numero > 75 and numero <= 100:
        conta_4 += 1 
         
print(f"{conta_1} foi numero de vezes que o numero inserido esteve entre [0-25] ")
print(f"{conta_2} foi numero de vezes que o numero inserido esteve entre [26-50]")
print(f"{conta_3} foi numero de vezes que o numero inserido esteve entre [51-75]")
print(f"{conta_4} foi numero de vezes que o numero inserido esteve entre [76-100]")
    
    