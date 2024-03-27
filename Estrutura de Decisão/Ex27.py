morangos = float(input("Digite a quantidade em kg de morangos comprados:"))
maca = float(input("Digite a quantidade em kg de maças compradas:"))

if morangos <= 5:
    valor_morangos = 2.50 * morangos
if maca <= 5:
    valor_maca = 1.80 * maca
if morangos > 5:
    valor_morangos = 2.20 * morangos
if maca > 5:
    valor_maca = 1.50 * maca

if morangos >= 8 or valor_morangos > 25:
    desconto = 0.10
    valor_morangos = valor_morangos - (valor_morangos * desconto)
if maca >= 8 or valor_morangos > 25:
    desconto = 0.10
    valor_maca = valor_maca - (valor_maca * desconto)

print(f"A quantidade de kg compradas de morango foi de {morangos:.2f} e o valor final de:{valor_morangos:.2f}R$")
print(f"A quantidade de kg compradas de maças foi de {maca:.2f} e o valor final de:{valor_maca:.2f}R$")

