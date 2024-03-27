#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

Turno = input("Digite em qual turno você estuda M-matutino ou V-Vespertino ou N- Noturno:")

if Turno == "M":
    print("BOM DIA !!!")
elif Turno == "V":
    print("BOA TARDE !!!")
elif Turno == "N":
    print("BOA NOITE !!!")    
else:
    print("Valor Inválido !!!")