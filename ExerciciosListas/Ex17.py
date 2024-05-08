'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e 
depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado 
o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
'''

atleta = []
salto1 = []
salto2 = []
salto3 = []
salto4 = []
salto5 = []
media = []
soma = 0
conta = 0
verifica = True

while verifica != False: 
    
    print("_"*50)
    atleta.append(input("Digite o nome do atleta:"))
    if atleta[conta] == "":
        verifica = False
        break
    else:
      salto1.append(float(input("Insira o primeiro salto:")))
      salto2.append(float(input("Insira o segundo salto:")))
      salto3.append(float(input("Insira o terceiro salto:")))
      salto4.append(float(input("Insira o quarto salto:")))
      salto5.append(float(input("Insira o quinto salto:")))
      
    conta += 1
      
for p,s,t,q,qui in zip(salto1,salto2,salto3,salto4,salto5):
        soma = soma + (p + s + t + q + qui)
        media.append(soma/5)
        soma = 0
        

for n,s1,s2,s3,s4,s5,mediaf in zip(atleta,salto1,salto2,salto3,salto4,salto5,media):
    if n == 0:
        print("Resultado final")
    print("_="*30)
    print(f"Nome do atleta:{n}")
    print(f"{s1}-{s2}-{s3}-{s4}-{s5}")
    print(f"Média dos saltos:{mediaf}")

    
       
    
