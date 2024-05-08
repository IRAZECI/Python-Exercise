'''Faça um Programa que peça as quatro notas de 10 alunos, 
calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.'''


notas = []
media = []
soma = 0
conta = 0

for i in range(0,10):
    print("_"*50)
    for e in range(0,4):
        notas.append(int(input(f"Insira a {e+1}° nota:")))
    
    for n in notas:
        soma = n + soma
        
    media.append(soma / 4)
       
    soma = 0
    notas.clear()
       
for m in media:   
  if m >= 7:
     conta += 1


    
print(f"{conta} alunos conseguiram uma media superior ou igual a 7.")
print(f"Medias: {media}")