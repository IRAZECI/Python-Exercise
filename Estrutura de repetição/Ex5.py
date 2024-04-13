#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
populacaoA = float(input("Digite o numero de habitantes da população A:"))
taxaA = int(input("Digite a taxa de crecimento A:"))
populacaoB = float(input("Digite o numero de habitantes da população B:"))
taxaB = int(input("Digite a taxa de crecimento B:"))

contador = 0
taxaA_f = taxaA / 100
taxaB_f = taxaB / 100

while populacaoA < populacaoB:
    populacaoA = populacaoA + (populacaoA * taxaA_f)
    populacaoB = populacaoB + (populacaoB * taxaB_f) 
    contador += 1
else:
    print(f"População A: {populacaoA} habitantes.")
    print(f"População B: {populacaoB} habitantes.")
    print(f"Demorou {contador} anos para que a população A supere a população B.")
