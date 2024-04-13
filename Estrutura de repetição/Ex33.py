#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
temp = 0
maior_t = 0
menor_t = 9999
media_t = 0
media_f = 0
c = 0

print("_"*30)
print("COD:-274 OUT")

while temp != -274:
    temp = int(input("Insira a temperatura:"))
    if temp == -274:
        break
    else:
      if temp > maior_t:
        maior_t = temp
      if temp < menor_t:
        menor_t = temp
      media_t = temp + media_t
      c += 1

media_f = media_t / c

print(f"A média das temperaturas é de:{media_f}°")
print(f"A maior temperatura é de:{maior_t}°")
print(f"A menor temperatura é de:{menor_t}°")