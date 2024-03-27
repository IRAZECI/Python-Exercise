#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.

valor_saque = float(input("Digite o valor que deseja sacar:"))

notas_100 = valor_saque // 100
valor_saque %= 100

notas_50 = valor_saque // 50
valor_saque %= 50

notas_10 = valor_saque // 10
valor_saque %= 10

notas_5 = valor_saque // 5
valor_saque %= 5 

notas_1 = valor_saque

print("NOTAS FORNECIDAS:")
print(f"Notas de 100:{notas_100}")
print(f"Notas de 50:{notas_50}")
print(f"Notas de 10:{notas_10}")
print(f"Notas de 5:{notas_5}")
print(f"Notas de 1:{notas_1}")