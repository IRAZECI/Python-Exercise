#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
#Código da cidade;
#Número de veículos de passeio (em 1999);
#Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#Qual a média de veículos nas cinco cidades juntas;
#Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio


conta = 1
a_a = 0
b_a = 9999999
media = 0
conta_2 = 0
media_a = 0


print("_"*50)
while conta <= 5:
    codigo = int(input("Insira o código da cidade:"))
    q_carros = int(input("Insira a quantidade de carros existentes na cidade:"))
    q_acidentes = int(input("Insira a quantidade de acidentes com vitimas:"))
    print("_"*50)

    media = q_carros + media

    if q_acidentes > a_a:
        a_a = q_acidentes
        codigo_a_a = codigo
    if q_acidentes < b_a:
        b_a = q_acidentes
        codigo_b_a = codigo
    if q_carros < 2000:
        media_a = media_a + q_acidentes
        conta_2 += 1 


    conta += 1

    media_f = media / 5
    media_f_b = media_a / conta_2

print("_"*50)
print(f"O maior índice de acidentes pertence a cidade {codigo_a_a} com {a_a} acidentes.")
print(f"O menor índice de acidentes pertence a cidade {codigo_b_a} com {b_a} acidentes.")
print(f"A media de veículos das 5 cidades juntas é de {media_f}.")
print(f"A média de acidentes nas cidades com menos de 2000 habitantes foi de {media_f_b}.")

