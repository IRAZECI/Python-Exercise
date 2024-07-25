"""
Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e
devolva uma string no formato D de mesPorExtenso de AAAA. 
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
"""
def convertemes(valor):
    meses = ['','janeiro','fevereiro','março','abril','maio', 
             'junho', 'julho' , 'agosto', 'setembro' , 'outubro',
             'novembro','dezembro']
    
    return meses[valor]
    
def datamostra(data):
    dia, mes, ano = data.split("/")
    mes = int(mes)
    if mes == 0 or mes > 12:
        print("Mês inválido")
        return False
    mes_extenso = convertemes(valor=mes)
    return f"{dia} de {mes_extenso} de {ano}"

print("_"*40)
data = input("Insira uma data no formato DD/MM/AAAA:")   

data_nova = datamostra(data=data)

print("--Novo formato--")
print(data_nova)