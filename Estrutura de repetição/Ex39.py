#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
conta = 1
altura_a = 0
altura_b = 9999

while conta <= 10:
    aluno = int(input("Insira o numero do aluno:"))
    altura = float(input("Insira a altura do aluno em cm:"))

    if altura > altura_a:
        altura_a = altura
        cod_aa = aluno
    if altura < altura_b:
        altura_b = altura
        cod_ab = aluno
    
    conta += 1

print(f"O aluno mais alto é de numero {cod_aa} com {altura_a:.2f}cm.")
print(f"O aluno mais baixo é o numero {cod_ab} com {altura_b:.2f}cm.")        
    