#Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. 
# A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). 
# As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

atleta = 'a'
nota = []
mai_n = 0
men_n = 0
soma = 0

while atleta != "":
    print("-="*50)
    atleta = input("Digite o nome do atleta:")
    
    if atleta != "":
      for i in range(0,7):
        nota.append(float(input(f"Insira a {i+1} nota:")))
        if i == 0:
            men_n = mai_n = nota[i]
        else:
            if mai_n > nota[i]:
                mai_n = nota[i]
            if men_n < nota[i]:
                men_n = nota[i]
    
    for s in nota:
        soma = soma + s
    
    media = (soma - (mai_n + men_n)) / 5
        
    print("_"*50)
    print(f"Atleta:{atleta}")
    for i,n in enumerate(nota,1):
        print(f"{i}° Salto: {n}")
    print()
    print("Resultado Final")
    print(f"Atleta:{atleta}")
    print(f"Melhor nota:{men_n}")
    print(f"Pior nota:{mai_n}")
    print(f"Média:{media}")
    
    nota = []
    mai_n = 0
    men_n = 0
    soma = 0
    media = 0   
        
        
    