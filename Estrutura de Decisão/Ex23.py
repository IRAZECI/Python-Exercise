n = float(input("Insira um numero:"))

n_r = round(n)

if n_r == n:
    print(f"O numero {n} é inteiro.")
else:
    print(f"O numero {n} é decimal.")