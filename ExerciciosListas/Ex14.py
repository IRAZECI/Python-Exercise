"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como 
"Inocente".
"""
perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?","Já trabalhou com a vítima?" ]
respostas = []
conta = 0
resultado = 0

print('Insira (s) para sim e (n) para não')
for i in perguntas:
    respostas.append(input(f"{i}"))
    
for i in respostas:
       if i == 's':
        conta += 1
        
if conta == 2:
    resultado = "Suspeita"
    
if conta == 3 or conta == 4:
    resultado = "Cúmplice"
    
if conta == 5:
    resultado = "Assassino"

if conta == 0 or conta == 1:
    resultado = "Inocente"
    
print(f"Com base nas respostas da pessoa sobre a participação no crime declaro: {resultado}")