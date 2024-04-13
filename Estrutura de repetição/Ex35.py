#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
print("_"*50)
print("LISTA GERADORA DE NUMEROS PRIMOS")
numero_1 = int(input("Insira o numero:"))

#Primeira iteração (Dar suporte a verificação)
for numero in range(1,numero_1+1):
  div = 0
#Segunda iteração (Verificar se é primo)
  for c in range(1,numero+1):
      if numero % c == 0:
         div += 1 

  if div == 2:
    print(f"O numero {numero} é primo.")
  else:
    print(f"O numero {numero} não é primo.")

