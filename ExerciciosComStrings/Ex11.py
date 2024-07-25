"""Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um 
arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado."""
import random

#Abrir arquivo txt
with open("texto1.txt", "r") as arquivo:
    conteudo = arquivo.read()

#__________________________________________________________________________________________________________
    
conteudo_lista = []
conteudo_lista = conteudo.split() #Estruturar palavras do aquivo texto em uma lista e inserir em uma lista 
random.shuffle(conteudo_lista) #Embaralha os itens da lista
palavra_escolhida = conteudo_lista[1] #Escolhe uma palavra aleatoria na lista
palavra_escolhida = list(palavra_escolhida) #Separa a palavra escolhida em letras (Facilitando a comparação nas proximas etapas)

#__________________________________________________________________________________________________________

print("JOGO DA FORCA") #Designer jogo
print("___________")
print("|          |")
print("|          O")
print("|         -|-")
print("|         //")
print("|          ")
letra = ""
conta_acerto = 0 
conta_erro = 0
tamanho_palavra = len(palavra_escolhida)
print("_"*tamanho_palavra)
letras_corretas = [] #Cria uma lista para captar as letras corretas inseridas pelo usuário
            
            


while conta_erro <= 6: #Se a quantidade de erro for maior que 6 o programa se encerra
    
    letra = input("\nInsira uma letra:") #Usuário insere a letra da rodada
    
    for i in palavra_escolhida: #Loop para identificar de a letra inserida está na palavra escolhida
        l = letra
        if l == i:
            print(f"\n{l} está presente na palavra escolhida")
            for l_p_e in palavra_escolhida:
                if l == l_p_e: #Verifica se a letra inserida pelo usuário está presenta na palavra escolhida
                    conta_acerto += 1 #Caso sim acrecenta um ponto de acerto
                    letras_corretas.append(l) #Lista das letras acertadas pelo usuário
#_____________________IMPORTANTE \/ _________________________________________________________                
                
                if l_p_e in letras_corretas: #Caso a letra da palavra escolhida esteja presente na lista de letras corretas inseridas pelo usuário
                    print(l_p_e,end="") #Exibisse a letra  
                else:
                    print("_",end="") #Caso não: Exibisse "_"
#_____________________________________________________________________________________________     
            
            else:
                break
            
              
        
                
    else:
        conta_erro += 1 #Caso depois de todo processo de iteração e comparação não for achado letra semelhente conta erro recebe 1
        print(f"\n{l} não está presente na palavra escolhida")
    
           
    
    if conta_acerto == len(palavra_escolhida): #caso numero de acertos seja igual ao numero de letras o jogador ganha
        print("\n\nVOCÊ GANHOU")
        break

        
    