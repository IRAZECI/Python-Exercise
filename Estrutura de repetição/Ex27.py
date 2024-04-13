#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
print('_'*30)
print('CALCULADOR DE MEDIA: ALUNOS POR TURMA')
q_turma = int(input("Digite a quantidade de turmas:"))

media = 0


for c in range(1,q_turma+1):
    q_alunos = int(input(f"Digite a quantidade de alunos na {c}° turma:"))
    
    if c == 1 and q_alunos > 40:
        q_alunos = 0
        q_alunos = int(input(f"Digite a quantidade de alunos na {c}° turma NOVAMENTE (40 ALUNOS NO MAXIMO):"))
    
    while q_alunos > 40:
        q_alunos = int(input(f"Digite a quantidade de alunos na {c}° turma NOVAMENTE (40 ALUNOS NO MAXIMO):"))

    media = q_alunos + media 
    media_f = media / q_turma

print('_'*30)
print(f"Existem {q_turma} turmas com uma media de {media_f} alunos por turma.")

