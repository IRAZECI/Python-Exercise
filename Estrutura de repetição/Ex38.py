#Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:.Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;.Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
salario_inicial = int(input("Digite seu salario incial:"))
ano_entrada = int(input("Digite seu ano inicial na empresa:"))
ano_atual = int(input("Digite seu ultimo ano na empresa:"))
aumento = 0.015


while ano_entrada <= ano_atual:
   aumento_a = salario_inicial * aumento
   salario_inicial = salario_inicial + aumento_a
   aumento = aumento * 2
   ano_entrada +=1

print(f"O seu salário atual é de {salario_inicial:.2f}")
    


