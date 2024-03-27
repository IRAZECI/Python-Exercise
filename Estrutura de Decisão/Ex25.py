
p_1 = input("Telefonou para a vítima?")

p_2 = input("Esteve no local do crime?")

p_3 = input("Mora perto da vítima?")

p_4 = input("Devia para a vítima?")

p_5 = input("Já trabalhou com a vítima?")

soma = 0 

if p_1 == "sim":
    soma = soma + 1
if p_2 == "sim":
    soma = soma + 1
if p_3 == "sim":
    soma = soma + 1
if p_4 == "sim":
    soma = soma + 1    
if p_5 == "sim":
    soma = soma + 1

if soma == 2:
   print("Pessoa Suspeita")  
elif soma == 3 or soma == 4:
   print("Pessoa Cúmplice")  
elif soma == 5:
    print("Pessoa Assassino")  


