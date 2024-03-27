#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

salário = float(input("Digite o valor do seu salário:"))

if salário <=  280:
    valor_reajuste = (salário * 0.20)
    salário_reajuste = salário + valor_reajuste
    aumento_texto = "Aumento de 20%"
elif salário <= 700:
    valor_reajuste = (salário * 0.15)
    salário_reajuste = salário + valor_reajuste
    aumento_texto = "Aumento de 15%"
elif salário <= 1500:
    valor_reajuste = (salário * 0.10)
    salário_reajuste = salário + valor_reajuste
    aumento_texto = "Aumento de 10%"
elif salário >= 1501:
    valor_reajuste = (salário * 0.05)
    salário_reajuste = salário + valor_reajuste
    aumento_texto = "Aumento de 5%"    

print(f"Salário anterior era de:{salário}R$\n")
print(f"{aumento_texto}\n")
print(f"Valor do aumento:{valor_reajuste}R$\n")
print(f"O valor do salário reajustado é de:{salário_reajuste}\n")

