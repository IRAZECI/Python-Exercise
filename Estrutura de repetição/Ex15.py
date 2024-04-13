#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
print("-"*30)
n = int(input("Digite o n_ésimo termo da série de Fibonacci:"))

conta = 2
t1 = 0
t2 = 1
print('{},{}'.format(t1,t2),end='')


while n >= conta:
    t3 = t1 + t2
    conta += 1
    t1 = t2
    t2 = t3
    print(',{}'.format(t3),end='')


