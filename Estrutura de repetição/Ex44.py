#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:

votar = 1
conta_1 = 0
conta_2 = 0
conta_3 = 0
conta_4 = 0
conta_5 = 0
conta_6 = 0


while votar != 0:
    
    print("_"*50)
    print("1 - Julio")
    print("2 - Jose")
    print("3 - Carlos")
    print("4 - Maria")
    print("5 - Voto nulo")
    print("6 - Voto em branco")
    print("_"*50)
    
    votar = int(input("Insira seu voto:"))
    
    if votar == 1:
        conta_1 += 1
    if votar == 2:
        conta_2 += 1
    if votar == 3:
        conta_3 += 1
    if votar == 4:
        conta_4 += 1
    if votar == 1:
        conta_5 += 1
    if votar == 1:
        conta_6 += 1

total_votos = conta_1 + conta_2 + conta_3 + conta_4 + conta_5 + conta_6

Porcentagem_votos_nulos = (conta_5 / total_votos) * 100
Porcentagem_votos_branco = (conta_6 / total_votos) * 100

print("_"*50)        
print(f"O total de votos foi de: {total_votos}")
print(f"O total de votos para o 1° foi de:{conta_1}")   
print(f"O total de votos para o 2° foi de:{conta_2}")     
print(f"O total de votos para o 3° foi de:{conta_3}")   
print(f"O total de votos para o 4° foi de:{conta_4}")    
print("_"*50)  
print(f"O total de votos nulos foi de: {conta_5}")
print(f"O total de votos em branco foi de: {conta_6}")
print("_"*50)  
print(f"A porcentagem  de votos nulos sobre o total de votos:{Porcentagem_votos_nulos:.2f}")
print(f"A porcentagem de votos em branco sobre o total de votos.:{Porcentagem_votos_branco:.2f}")
