"""
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""
verifica = True
verifica_entrada = 0
mouses = []
conta = 0

print("1- necessita da esfera\n2- necessita de limpeza\n3- necessita troca do cabo ou conector\n4- quebrado ou inutilizado")
print("_"*40)
while verifica == True: #Coleta problemas do mouse
    verifica_entrada = int(input(f"Digite o problema do {conta+1}° mouse:"))
    if verifica_entrada == 0:
        verifica = False
        break
    else:
        mouses.append(verifica_entrada)
        
    verifica_entrada = 0
    conta += 1
 
problema1 = 0
problema2 = 0
problema3 = 0
problema4 = 0 
  
for m in mouses: #Verifica qual é o tipo de problema
    if m == 1:
        problema1 += 1
    if m == 2:
        problema2 += 1
    if m == 3:
        problema3 += 1
    if m == 4:
        problema4 += 1
        
def porcentual(p,t):
    return p / t * 100

porcentual1 = porcentual(problema1,conta)
porcentual2 = porcentual(problema2,conta)
porcentual3 = porcentual(problema3,conta)
porcentual4 = porcentual(problema4,conta)

print("_"*40)
print("Quantidade de mouses: {}".format(conta))
print(f"Situação                        Quantidade              Percentual")
print(f"1- necessita da esfera                  {problema1}                     {porcentual1:.2f}%")
print(f"2- necessita de limpeza                 {problema2}                     {porcentual2:.2f}%")
print(f"3- necessita troca do cabo ou conector  {problema3}                     {porcentual3:.2f}%")
print(f"4- quebrado ou inutilizado              {problema4}                     {porcentual4:.2f}%")