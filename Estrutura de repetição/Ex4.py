#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
populacaoA = 80000 
populacaoB = 200000 
conta_ano = 0
while populacaoA < populacaoB:
    populacaoA = populacaoA * 1.03
    populacaoB = populacaoB * 1.015
    conta_ano += 1
    print(f"Cidade a população:{populacaoA}")
    print(f"Cidade b população:{populacaoB}")
    print(f"Quantidade de anos:{conta_ano}")
else:
    print(f"Demorou {conta_ano} anos para a cidade a superar a cidade b.")