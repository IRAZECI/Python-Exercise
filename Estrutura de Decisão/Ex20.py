n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
n3 =float(input("Digite a terceira nota:"))

media = (n1 + n2 + n3) / 3

if media == 10:
    print(f"Sua media foi de {media:.2f}, você está APROVADO com Distinção.")
elif media >= 7:
    print(f"Sua media foi de {media:.2f}, você está APROVADO.")
elif media < 7:
    print(f"Sua media foi de {media:.2f}, você está REPROVADO.")


