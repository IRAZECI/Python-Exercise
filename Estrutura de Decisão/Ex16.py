#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
a = int(input("Digite o valor do coeficiente A:"))
if  a == 0:
    print("O valor de A é igual a zero,a equação não é do segundo grau.")
    exit()
b = int(input("Digite o valor do coeficiente B:"))
c = int(input("Digite o valor do coeficiente C:"))
print("\n")



# delta = b^2 - 4ac 
delta = b**2 - 4*a*c
if delta < 0:
    print("A equação não possui raizes reais.")
    exit()
print(f"O valor de delta é:{delta}\n")
if delta == 0:
    print("A equação possui apenas uma raiz real.")
    print("\n")
# x = (-b +- raiz(delta)) / 2a 
# delta elavado a meia é a mesma coisa que raiz quadrada

x1 = (-b - delta**0.5) / (2*a)
x2 = (-b - delta**0.5) / (2*a)

print(f"O valor de x1 é de:{x1}\n")
print(f"O valor de x2 é de:{x2}\n")




