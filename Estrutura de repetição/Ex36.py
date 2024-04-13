#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
print("_"*30)
n_t = int(input("Montar tabuada de:"))
c_t = int(input("Começo da tabuada:"))
f_t = int(input("Final da tabuda:"))
resultado = 0

print(f"Vou montar a tabuda de {n_t}, começando no numero {c_t} e terminando no {f_t}.")

for c in range(c_t,f_t +1):
    resultado = n_t * c
    print(f"{n_t}X{c}={resultado}")
    c += 1
    resultado = 0
