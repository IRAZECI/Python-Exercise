#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

atleta = "a"
saltos = []
mai_n = 0
men_n = 0
soma = 0

print("-="*50)
while atleta != "":
    atleta = input("Digite o nome do atleta:")
    if atleta != "":
       for c in range(0,5):
          saltos.append(float(input(f"Digite o {c+1}° salto do atleta:")))
          if c == 0:
              mai_n = men_n = saltos[c]
          else:
              if saltos[c] > mai_n:
                  mai_n = saltos[c]
              if saltos[c] < men_n:
                  men_n = saltos[c]
    
    for n in saltos:
       soma = n + soma
    
    media = (soma - (mai_n + men_n)) / 3 
    
    print("-="*50)
    print(f"Atleta:{atleta}")
    print()
    for e,n in enumerate(saltos):
        print(f"Altura do {e+1}° salto:{n} m")
    print()
    print(f"O melhor salto foi {mai_n} m")
    print(f"O pior salto foi {men_n} m")
    print(f"A media dos demais saltos foi de {media} m")
    print("-="*50)
    print()
    print(f"Resultado final:")
    print(f"{atleta} - {media} m")
    print()
    
    saltos = []
    mai_n = 0
    men_n = 0
    soma = 0




               