#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

nota_1 = float(input("Digite sua primeira nota:"))
nota_2 = float(input("Digite sua segunda nota:"))

media_geral = (nota_1 + nota_2) / 2

if media_geral < 4.0:
  conceitos = "E"
elif media_geral < 6.0:
    conceitos = "D"
elif media_geral < 7.5:
    conceitos = "C"
elif media_geral < 9.0:
    conceitos = "B"
elif media_geral < 10.0:
    conceitos = "A"

if conceitos == "D" or conceitos == "E":
   mensagem = "REPROVADO"
elif conceitos == "A" or conceitos == "B" or conceitos == "C":
    mensagem = "APROVADO"   


print(f"Nota 1: {nota_1}\nNota 2: {nota_2}")
print(f"Media: {media_geral}\nConceito: {conceitos}\nVocê está:{mensagem}")

