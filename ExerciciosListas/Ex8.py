'''
Faça um Programa que peça a idade e a altura de 5 pessoas, 
armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.

'''

idade = []
altura = []

for i in range(0,3):
    idade.append(int(input(f"Insira a {i+1}° idade:")))
print("_"*50)   
for i in range(0,3):
    altura.append(float(input(f"Insira a {i+1}° altura:")))
    
idade.reverse()
altura.reverse()
    
print("_"*50)
print(f"Idade inseridas na ordem inversa:{idade}")
print(f"Altura inseridas na ordem inversa:{altura}")

