litros_v = float(input("Digite a quantidade de litros vendidos:"))

combustivel = input("Digite o tipo de combustivel:")

if combustivel == "a" and litros_v <= 20:
    valor = (litros_v * 1.90) - (litros_v * 0.03)

elif combustivel == "a" and litros_v > 20:
    valor = (litros_v * 1.90) - (litros_v * 0.05)

elif combustivel == "g" and litros_v <= 20:
    valor = (litros_v * 2.50) - (litros_v * 0.04)
    
elif combustivel == "g" and litros_v > 20:
    valor = (litros_v * 2.50) - (litros_v * 0.06)

print(f"O valor a ser pago é de {valor}")
