'''
Faça um programa que leia um número indeterminado de valores, 
correspondentes a notas, encerrando a entrada de dados quando for 
informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
'''

valores = []
soma = 0
media = 0
verificar = 1
conta = 0
conta_2 = 0
conta_3 = 0

print("_"*50)
while verificar >= 0:
    verificar = float(input("Insira qualquer valor acima de -1:"))
    if verificar >= 0:
      valores.append(verificar)
      conta += 1
      
for i in valores:
  soma = soma + i
  
media = soma / len(valores)

for i in valores:
  if i > media:
    conta_2 += 1
    
for i in valores:
  if i > 7:
    conta_3 += 1
    

      
   
print("_"*50)
print(f"A quantidade de valores lidos pelo programa foram de:{conta}")
print(f"Valores informados na ordem que foram inseridos:{valores}")
print(f"Valores informados na ordem inversa à que foram informados:{valores[::-1]}")
print(f"A soma de todos os valores inseridos foi de:{soma}")
print(f"A média de todos os valores inseridos foi de:{media}")
print(f"Quantidade de valores acima da média calculada:{conta_2}")
print(f"Quantidade de valores abaixo de 7:{conta_3}")
print(f"PROGRAMA ENCERRADO")

