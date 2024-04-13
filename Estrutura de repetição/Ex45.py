#Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
#Maior e Menor Acerto;
#Total de Alunos que utilizaram o sistema;
#A Média das Notas da Turma.
#Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

confirma = 's'
conta = 0
conta_acerto = 0
media_acerto = 0
maior_acerto = 0
menor_acerto = 11

print("_"*50)
print("GABARITO DA PROVA")
r_1 = input("Insira 1° resposta:")
r_2 = input("Insira 2° resposta:")
r_3 = input("Insira 3° resposta:")
r_4 = input("Insira 4° resposta:")
r_5 = input("Insira 5° resposta:")
r_6 = input("Insira 6° resposta:")
r_7 = input("Insira 7° resposta:")
r_8 = input("Insira 8° resposta:")
r_9 = input("Insira 9° resposta:")
r_10 = input("Insira 10° resposta:")



while confirma == 's' or confirma == "S":
    if conta != 0:
        confirma = input("Outro aluno deseja ultilizar o sistema:")
    if confirma != 's' or confirma == "S":
        break
    
    print("_"*50)
    print("VERIFICADOR DE NOTAS")
    q_1 = input("Qual é a resposta da 1° questão:")
    q_2 = input("Qual é a resposta da 2° questão:")
    q_3 = input("Qual é a resposta da 3° questão:")
    q_4 = input("Qual é a resposta da 4° questão:")
    q_5 = input("Qual é a resposta da 5° questão:")
    q_6 = input("Qual é a resposta da 6° questão:")
    q_7 = input("Qual é a resposta da 7° questão:")
    q_8 = input("Qual é a resposta da 8° questão:")
    q_9 = input("Qual é a resposta da 9° questão:")
    q_10 = input("Qual é a resposta da 10° questão:")
    
    if q_1 == r_1:
        conta_acerto += 1
    if q_2 == r_2:
        conta_acerto += 1
    if q_3 == r_3:
        conta_acerto += 1
    if q_4 == r_4:
        conta_acerto += 1
    if q_5 == r_5:
        conta_acerto += 1
    if q_6 == r_6:
        conta_acerto += 1
    if q_7 == r_7:
        conta_acerto += 1
    if q_8 == r_8:
        conta_acerto += 1
    if q_9 == r_9:
        conta_acerto += 1
    if q_10 == r_10:
        conta_acerto += 1
        
    conta += 1
    
    media_acerto = conta_acerto + media_acerto  
    media_acerto_final = media_acerto / conta
    
    if conta_acerto > maior_acerto:
        maior_acerto = conta_acerto
    
    if conta_acerto < menor_acerto:
        menor_acerto = conta_acerto
    
    conta_acerto = 0


print("_"*50)
print(f"A maior quantidade de acertos foi de {maior_acerto} questões.")
print(f"A menor quantidade de acertos foi de {menor_acerto} questões.")
print(f"A media de notas foi de {media_acerto_final}.")
print(f"Total de {conta} alunos utilizaram o sistema.")
print("_"*50)


    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    