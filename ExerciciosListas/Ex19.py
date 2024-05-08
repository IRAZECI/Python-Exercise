"""
Uma empresa de pesquisas precisa tabular os resultados da seguinte 
enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

"""
votos = []
votos_totais = []
porcentagem_total = []
verifica_voto = 0
verifica = True
maior_voto = 0
maior_porcentagem = 0
conta = 0
voto1 = 0
voto2 = 0
voto3 = 0
voto4 = 0
voto5 = 0
voto6 = 0
vencedor = ''


def porcentagem(v,tv):
    return (v / tv) * 100


print("Qual o melhor Sistema Operacional para uso em servidores?\nAs possíveis respostas são:")
print("1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro")

while verifica == True: #COLETOR DE VOTOS
    verifica_voto = int(input(f"Insira o {conta+1}° voto:"))
    if verifica_voto == 0:
        verifica = False
        break
    elif verifica_voto > 6:
        print("Voto inserido ínvalido")
    else:
        votos.append(verifica_voto)
        
    verifica_voto = 0
    conta += 1
    
for v in votos: #Analisador dos votos
    if v == 1:
        voto1 += 1  
    if v == 2:
        voto2 += 1   
    if v == 3:
        voto3 += 1   
    if v == 4:
        voto4 += 1   
    if v == 5:
        voto5 += 1   
    if v == 6:
        voto6 += 1   
 
votos_totais.extend((voto1,voto2,voto3,voto4,voto5,voto6))
 
for v in votos_totais:
    if v > maior_voto:
        maior_voto = v
    
if voto1 == maior_voto:
    vencedor = 'Windows Server'
if voto2 == maior_voto:
    vencedor = 'Unix'
if voto3 == maior_voto:
    vencedor = 'Linux'
if voto4 == maior_voto:
    vencedor = 'Netware'
if voto5 == maior_voto:
    vencedor = 'Mac OS'
if voto6 == maior_voto:
    vencedor = 'Outro'

    
porcentagem1 = porcentagem(voto1,conta)
porcentagem2 = porcentagem(voto2,conta)
porcentagem3 = porcentagem(voto3,conta)
porcentagem4 = porcentagem(voto4,conta)
porcentagem5 = porcentagem(voto5,conta)
porcentagem6 = porcentagem(voto6,conta)   

porcentagem_total.extend((porcentagem1,porcentagem2,porcentagem3,porcentagem4,porcentagem5,porcentagem6))

for p in porcentagem_total:
    if p > maior_porcentagem:
        maior_porcentagem = p
        

print("Sistema Operacional     Votos   %")
print("-------------------     -----   ---")
print(f"Windows Server          {voto1}     {porcentagem1:.2f}% ")
print(f"Unix                    {voto2}     {porcentagem2:.2f}% ")
print(f"Linux                   {voto3}     {porcentagem3:.2f}% ")
print(f"Netware                 {voto4}     {porcentagem4:.2f}% ")
print(f"Mac OS                  {voto5}     {porcentagem5:.2f}% ")
print(f"Outro                   {voto6}     {porcentagem6:.2f}% ")

print(f"O Sistema Operacional mais votado foi o {vencedor}, com {maior_voto} votos, correspondendo a {maior_porcentagem:.2f}% dos votos.")