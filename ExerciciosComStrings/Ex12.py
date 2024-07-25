""" Valida e corrige número de telefone. Faça um programa que leia um número de telefone, 
e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. 
O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133 """

print("_"*30)
print("Valida e corrige números de telefone")
numero_telefone = input("Insira um numero de telefone:")

numero_telefone = list(numero_telefone)

t_t = numero_telefone.count("-")

if t_t > 0: #Se conter -
    if len(numero_telefone) == 8: #Se conter 7 dígitos (contando com -)
        print("_"*30)
        
        n_t_1 = "".join(numero_telefone)
        
        print(f"Telefone corrigido sem formatação:{n_t_1}")
        print("Telefone possuí 7 dígitos,Irei acrecentar o digito três na frente...")
        
        numero_telefone.append("3")
        n_t_2 = "".join(numero_telefone)
        print(f"Telefone corrigido com formatação:{n_t_2}")

else: #Se não conter -
    print("_"*30)
    
    n_t_1 = "".join(numero_telefone)
    print(f"Telefone corrigido sem formatação:{n_t_1}")
    print("Telefone não possuí traço separador,Irei acrecentar o caractere...")
    numero_telefone.insert(3,"-")
    
    if len(numero_telefone) == 8:  #Se conter 7 dígitos  
       numero_telefone.append("3")
       print("Telefone possuí 7 dígitos.Irei acrecentar o digito três na frente...")  
       
    n_t_2 = "".join(numero_telefone)  
    print(f"Telefone corrigido com formatação:{n_t_2}")

