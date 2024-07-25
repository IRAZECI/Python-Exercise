"""  
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. 
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para
efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. 
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de 
entrada todas as vezes que desejar.
"""

def conv_hora(hora,minutos):
    if hora == 13:
        h = 1
    elif hora == 14:
        h = 2
    elif hora == 15:
        h = 3
    elif hora == 16:
        h = 4 
    elif hora == 17:
        h = 5
    elif hora == 18:
        h = 6
    elif hora == 19:
        h = 7
    elif hora == 20:
        h = 8
    elif hora == 21:
        h = 9
    elif hora == 22:
        h = 10
    elif hora == 23:
        h = 11
    elif hora == 24:
        h = 0
    else:
        h = hora
        
    m = minutos   
    
    if hora >=13:
        ap = "P.M"
    else:
        ap = "A.M"
        
    return h,m,ap
           
hora = int(input("Insira a hora:"))
minutos = int(input("Insira os minutos:"))

hora_min_cov = conv_hora(hora, minutos)

def saida(hora_convertida):
    conta = 0
    for hora in hora_convertida:
        if conta == 0:
           h = hora
        elif conta == 1:
           m = hora
        elif conta == 2:
            ap = hora
        conta += 1
    
        
    h = str(h)
    m = str(m)
    ap = str(ap)
    
    
    h_m_ap = h+":"+m+" "+ap    
    
    return h_m_ap

hora_completa = saida(hora_min_cov)

print("_"*20)
print("HORA CONVERTIDA")
print(hora_completa)