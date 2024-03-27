#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

lado_1 = float(input("Digite o tamanho do primeiro lado:")) 
lado_2 = float(input("Digite o tamanho do segundo lado:")) 
lado_3 = float(input("Digite o tamanho do terceiro lado:")) 

verificador = 0
tipo_triangulo = 0

if lado_1 + lado_2 > lado_3:
   verificador = "É um Triângulo"
else: 
    verificador = "Não é um triângulo"   
    
if verificador == "É um Triângulo":
   if lado_1 == lado_2 == lado_3:
    tipo_triangulo = "Equilátero"
   elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3:
    tipo_triangulo = "Isósceles"
   elif lado_1 != lado_2 != lado_3:
    tipo_triangulo = "Escaleno"
else:
    tipo_triangulo = "Não existe"


print(f"{verificador}\n")
print(f"O tiangulo do tipo: {tipo_triangulo}\n")
