modelo_carro = []
km_litro = []
consumo_1000 = []
valor_1000 = []
verifica = True
verifica_carro = ''
mais_economico_nome = ''
mais_economico = 9999999
verifica_km = 0
contador = 1
litro_gasolina = 2.25


print("Comparativo do Consumo de Combustível") 
while verifica == True: #Coleta Consumo e modelo
    print("\n")
    print(f"Veículo {contador}")
    print("_"*30)
    verifica_carro = input("Digite o nome do modelo:")
    if verifica_carro == '':
        verifica = False
        break
    else:
        modelo_carro.append(verifica_carro)
        
    verifica_km = float(input("Km por litro:"))    
    if verifica_km == 0:
        print("Valor inserido é inválido")
    else:
       km_litro.append(verifica_km)
        
    verifica_carro = 0
    verifica_km = 0
    contador += 1
    
for c_km in km_litro:
    consumo_1000.append(1000/c_km)
    
for c_km in consumo_1000:  
    valor_1000.append(c_km*litro_gasolina)
  
contador = 1  
    
print("Relatório Final")
print("_"*30)
for n_v,k_l,mil_l,v_t in zip(modelo_carro,km_litro,consumo_1000,valor_1000):
    print(f" {contador} - {n_v}           -    {k_l} -  {mil_l:.2f} litros - R$ {v_t:.2f}")
    
    contador += 1 
    
for km_l,m_v in zip(km_litro,modelo_carro):
    if km_l < mais_economico:
        km_l = mais_economico
        mais_economico_nome = m_v
        
              
print(f"O menor consumo é {mais_economico_nome}")