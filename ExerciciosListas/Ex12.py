"""
Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura 
inferior à média de altura desses alunos.   
"""
idades = []
alturas = []
soma = 0
conta = 0

for i in range(0,30):
    idades.append(int(input(f"Insira a idade do {i+1}° aluno:")))
    
for i in range(0,30):
    alturas.append(float(input(f"Insira a altura do {i+1}° aluno:")))
    
for i in alturas:
    soma = i + soma
    media_altura = soma / len(alturas)
    
for a,b in zip(idades, alturas):
    if a > 13 and b < media_altura:
        conta += 1 
        
print(f'Idades dos alunos:{idades}')
print(f'Altura dos alunos:{alturas}')
print(f'Quantidade de alunos com mais de 13 anos que possuem altura inferior á média de altura dos demais alunos:{conta}')