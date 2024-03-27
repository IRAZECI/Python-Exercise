#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
print("Digite uma data no formato (dd/mm/aaaa)")

data_dia = int(input("Digite qual é o dia:"))
if data_dia > 31:
    print("Valor inválido")
    exit()

data_mes = int(input("Digite qual é o mês:"))

if  data_mes > 12:
    print("Valor inválido")
    exit()

data_ano = int(input("Digite qual é o ano:"))

if  data_ano > 9999:
    print("Valor inválido")
    exit()
   

print(f"A data inserida é válida:{data_dia}/{data_mes}/{data_ano}")

