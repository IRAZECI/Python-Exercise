'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).'''
temp_media = []
mes = ['janeiro', "Fevereiro", "Março", "Abril","Maio","Junho", "Julho", "Agosto", "Setembro","Outubro","Novembro","Dezembro"]
mes_valido = []
soma = 0
media = 0


for i in range(0,12):
   temp_media.append(float(input(f"Insira a média de temperatura do {i+1}° mês:")))

for i in temp_media:
    soma = soma + i
    
media = soma / len(temp_media)

for t,m in zip(temp_media,mes):
    if t > media:
        mes_valido.append(m)
    
print("=-"*35)
print(f"A média anual de temperatura foi de: {media}")
print(f"As médias de temperatura mensal foram: {temp_media}")
print(f"Os mêses que registraram temperatura maior do que a média anual foram: {mes_valido}")
print("=-"*35)  

    
   
        
        