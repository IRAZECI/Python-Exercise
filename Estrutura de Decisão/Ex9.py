#Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input("Digite o primeiro numero:"))
n2 = float(input("Digite o segundo numero:"))
n3 = float(input("Digite o terceiro numero:"))

if   n1 > n2 and n1 > n3 and n2 > n3:
   pri_n = n1
   sen_n = n2
   ter_n = n3
elif n1 > n2 and n1 > n3 and n3 > n2:
   pri_n = n1
   sen_n = n3
   ter_n = n2      
elif n2 > n1 and n2 > n3 and n1 > n3:
   pri_n = n2
   sen_n = n1
   ter_n = n3
elif n2 > n1 and n2 > n3 and n3 > n1:
   pri_n = n2
   sen_n = n3
   ter_n = n1 
elif n3 > n1 and n3 > n2 and n1 > n2:
   pri_n = n3
   sen_n = n1
   ter_n = n2
elif n3 > n1 and n3 > n2 and n2 > n1:
   pri_n = n3
   sen_n = n2
   ter_n = n1    
           
print(f"Primeiro numero:{pri_n:.2f}\n")           
print(f"Segundo numero:{sen_n:.2f}\n")
print(f"Terceiro numero:{ter_n:.2f}\n")







