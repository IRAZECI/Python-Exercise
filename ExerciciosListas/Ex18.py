"""
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador 
após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, 
para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de 
programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número 
da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for 
digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. 
Após o final da votação, o programa deverá exibir:
O total de votos computados;
Os númeos e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
    
"""
votos = [] #numero dos votos
todos_votos = []
verifica = True #verificador de finalizador
conta = 0 #total de votos 
melhor_jogador = 0
maior_porcentagem = 0
m = 0
voto1 = 0
voto2 = 0
voto3 = 0
voto4 = 0
voto5 = 0
voto6 = 0
voto7 = 0
voto8 = 0
voto9 = 0
voto10 = 0
voto11 = 0
voto12 = 0
voto13 = 0
voto14 = 0
voto15 = 0 
voto16 = 0
voto17 = 0
voto18 = 0
voto19 = 0
voto20 = 0
voto21 = 0
voto22 = 0
voto23 = 0

def porcentagem(numero_votos,contar):
    return (numero_votos / contar) * 100
    


while verifica == True:
    votos.append(int(input("Insira o numero do melhor jogador (digite 0 para sair):")))
    if votos[conta] == 0:
        verifica = False
        del votos[conta]
    else:
      while votos[conta] >= 24:
        print("Numero ínvalido,Insira novamente")
        votos.append(int(input("Insira o numero do melhor jogador (digite 0 para sair):")))
        del votos[conta]
      if votos[conta] == 0:
        verifica = False
        del votos[conta]
        
    conta += 1
    
for i in votos:
    if i == 1:
        voto1 += 1
    if i == 2:
        voto2 += 1
    if i == 3:
        voto3 += 1
    if i == 4:
        voto4 += 1    
    if i == 5:
        voto5 += 1     
    if i == 6:
        voto6 += 1     
    if i == 7:
        voto7 += 1      
    if i == 8:
        voto8 += 1      
    if i == 9:
        voto9 += 1
    if i == 10:
        voto10 += 1     
    if i == 11:
        voto11 += 1     
    if i == 12:
        voto12 += 1     
    if i == 13:
        voto13 += 1
    if i == 14:
        voto14 += 1 
    if i == 15:
        voto15 += 1 
    if i == 16:
        voto16 += 1 
    if i == 17:
        voto17 += 1 
    if i == 18:
        voto18 += 1 
    if i == 19:
        voto19 += 1 
    if i == 20:
        voto20 += 1 
    if i == 21:
        voto21 += 1 
    if i == 22:
        voto22 += 1     
    if i == 23:
        voto23 += 1 
     
 
        
             
conta = conta - 1 #correção numérica contador

porcentagem1 = porcentagem(voto1,conta)  
porcentagem2 = porcentagem(voto2,conta)  
porcentagem3 = porcentagem(voto3,conta)  
porcentagem4 = porcentagem(voto4,conta)  
porcentagem5 = porcentagem(voto5,conta)  
porcentagem6 = porcentagem(voto6,conta)  
porcentagem7 = porcentagem(voto7,conta)  
porcentagem8 = porcentagem(voto8,conta)  
porcentagem9 = porcentagem(voto9,conta)  
porcentagem10 = porcentagem(voto10,conta)  
porcentagem11 = porcentagem(voto11,conta)  
porcentagem12 = porcentagem(voto12,conta)  
porcentagem13 = porcentagem(voto13,conta)  
porcentagem14 = porcentagem(voto14,conta)  
porcentagem15 = porcentagem(voto15,conta)  
porcentagem16 = porcentagem(voto16,conta)  
porcentagem17 = porcentagem(voto17,conta)  
porcentagem18 = porcentagem(voto18,conta)  
porcentagem19 = porcentagem(voto19,conta)  
porcentagem20 = porcentagem(voto20,conta)  
porcentagem21 = porcentagem(voto21,conta)  
porcentagem22 = porcentagem(voto22,conta)  
porcentagem23 = porcentagem(voto23,conta)


print('\n')
print("_"*40)
print("Resultado da votação")
print(f"Foram computados {conta} votos")
print("Jogador     Votos       Porcentagem")
if voto1 > 0:
    print(f"1           {voto1}            {porcentagem1:.2f}")
if voto2 > 0:
    print(f"2           {voto2}            {porcentagem2:.2f}")
if voto3 > 0:
    print(f"3           {voto3}            {porcentagem3:.2f}")
if voto4 > 0:
    print(f"4           {voto4}            {porcentagem4:.2f}")
if voto5 > 0:
    print(f"5           {voto5}            {porcentagem5:.2f}")
if voto6 > 0:
    print(f"6           {voto6}            {porcentagem6:.2f}")
if voto7 > 0:
    print(f"7           {voto7}            {porcentagem7:.2f}")
if voto8 > 0:
    print(f"8           {voto8}            {porcentagem8:.2f}")
if voto9 > 0: 
    print(f"9           {voto9}            {porcentagem9:.2f}")
if voto10 > 0:
    print(f"10          {voto10}           {porcentagem10:.2f}")
if voto11 > 0:
    print(f"11          {voto11}           {porcentagem11:.2f}")
if voto12 > 0:
    print(f"12          {voto12}           {porcentagem12:.2f}")
if voto13 > 0:
    print(f"13          {voto13}           {porcentagem13:.2f}")
if voto14 > 0: 
    print(f"14          {voto14}           {porcentagem14:.2f}")
if voto15 > 0:
    print(f"15          {voto15}           {porcentagem15:.2f}")
if voto16 > 0:
    print(f"16          {voto16}           {porcentagem16:.2f}")
if voto17 > 0:
    print(f"17          {voto17}           {porcentagem17:.2f}")
if voto18 > 0:
    print(f"18          {voto18}           {porcentagem18:.2f}")
if voto19 > 0:
    print(f"19          {voto19}           {porcentagem19:.2f}")
if voto20 > 0:
    print(f"20          {voto20}           {porcentagem20:.2f}")
if voto21 > 0:
    print(f"21          {voto21}           {porcentagem21:.2f}")
if voto22 > 0:
    print(f"22          {voto22}           {porcentagem22:.2f}")
if voto23 > 0:
    print(f"23          {voto23}           {porcentagem23:.2f}")

todos_votos.append(voto1)
todos_votos.append(voto2)
todos_votos.append(voto3)
todos_votos.append(voto4)
todos_votos.append(voto5)
todos_votos.append(voto6)
todos_votos.append(voto7)
todos_votos.append(voto8)
todos_votos.append(voto9)
todos_votos.append(voto10)
todos_votos.append(voto11)
todos_votos.append(voto12)
todos_votos.append(voto13)
todos_votos.append(voto14)
todos_votos.append(voto15)
todos_votos.append(voto16)
todos_votos.append(voto17)
todos_votos.append(voto18)
todos_votos.append(voto19)
todos_votos.append(voto20)
todos_votos.append(voto21)
todos_votos.append(voto22)
todos_votos.append(voto23)


for v_t in todos_votos:
    if v_t > m:
        m = v_t
    

if m == voto1:
        melhor_jogador = 1
        maior_porcentagem = porcentagem1
if m == voto2:
        melhor_jogador = 2
        maior_porcentagem = porcentagem2
if m == voto3:
        melhor_jogador = 3
        maior_porcentagem = porcentagem3
if m == voto4:
        melhor_jogador = 4
        maior_porcentagem = porcentagem4
if m == voto5:
        melhor_jogador = 5
        maior_porcentagem = porcentagem5
if m == voto6:
        melhor_jogador = 6
        maior_porcentagem = porcentagem6
if m == voto7:
        melhor_jogador = 7
        maior_porcentagem = porcentagem7
if m == voto8:
        melhor_jogador = 8
        maior_porcentagem = porcentagem8
if m == voto9:
        melhor_jogador = 9
        maior_porcentagem = porcentagem9
if m == voto10:
        melhor_jogador = 10
        maior_porcentagem = porcentagem10
if m == voto11:
        melhor_jogador = 11
        maior_porcentagem = porcentagem11
if m == voto12:
        melhor_jogador = 12
        maior_porcentagem = porcentagem12
if m == voto13:
        melhor_jogador = 13
        maior_porcentagem = porcentagem13
if m == voto14:
        melhor_jogador = 14
        maior_porcentagem = porcentagem14
if m == voto15:
        melhor_jogador = 15
        maior_porcentagem = porcentagem15
if m == voto16:
        melhor_jogador = 16
        maior_porcentagem = porcentagem16
if m == voto17:
        melhor_jogador = 17
        maior_porcentagem = porcentagem17
if m == voto18:
        melhor_jogador = 18
        maior_porcentagem = porcentagem18
if m == voto19:
        melhor_jogador = 19
        maior_porcentagem = porcentagem19
if m == voto20:
        melhor_jogador = 20
        maior_porcentagem = porcentagem20
if m == voto21:
        melhor_jogador = 21
        maior_porcentagem = porcentagem21
if m == voto22:
        melhor_jogador = 22
        maior_porcentagem = porcentagem22
if m == voto23:
        melhor_jogador = 23
        maior_porcentagem = porcentagem23
    





print(f"O melhor jogador foi o número {melhor_jogador}, com {m} votos, correspondendo a {maior_porcentagem:.2f}% do total de votos.")
    


