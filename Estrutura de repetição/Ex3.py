#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = str(input("Digite seu nome:"))
while len(nome) <= 3:
    nome = str(input("Nome invalido,digite novamente:"))

idade = int(input("Digite sua idade:"))
while idade < 0 and idade > 150:
    idade = int(input("Idade invalida,digite novamente:"))

salario = float(input("Digite seu salário:")) 
while salario <= 0:
    salario = float(input("Salario invalido,digite novamente:")) 

sexo = str(input("Digite seu sexo:"))
while sexo != "f" and sexo != "m":
    sexo = str(input("Sexo invalido,digite seu sexo:"))

estado_civil = str(input("Digite seu estado civil:"))
while estado_civil !=  "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
    estado_civil = str(input("Estado civil invalido,digite novamente:"))

print("BEM VINDO, sua escrição foi bem sucedida")

