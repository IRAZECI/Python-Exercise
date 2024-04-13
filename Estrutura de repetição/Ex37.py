#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
print("_"*30)
print("PESQUISA DA ACADEMIA")
print("_"*30)

codigo = 1
altura = 0
peso = 0
conta = 0
media_a = 0
media_p = 0
altura_a = 0
altura_b = 9999
peso = 0
peso_a = 0
peso_b = 9999



while codigo != 0:
   codigo = int(input("Insira seu código:"))
   if codigo == 0:
      break
   altura = float(input("Insira sua altura:"))
   peso = float(input("Digite sua peso:"))
   print("_"*30)

   
   media_a = media_a + altura
   media_p = media_p + peso
   conta += 1 
   
   if altura > altura_a:
      altura_a = altura
      codigo_aa = codigo
   if altura < altura_b:
      altura_b = altura
      codigo_ab = codigo
   if peso > peso_a:
      peso_a = peso
      codigo_pa = codigo
   if peso < peso_b:
      peso_b = peso
      codigo_pb = codigo


media_a_f = media_a / conta
media_p_f = media_p / conta

print("_"*30)
print("RESULTADOS")
print("_"*30)

print(f"O mais alto cliente é o numero {codigo_aa}, com a altura de {altura_a}.")
print(f"O mais baixo cliente é o numero {codigo_ab},com a altura de {altura_b}.")
print(f"O mais gordo cliente é o numero {codigo_pa},com o peso de {peso_a}.")
print(f"O mais magro cliente é o numero {codigo_pb}, com o peso de {peso_b}.")
      

