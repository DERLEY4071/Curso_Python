#DESAFIO 02

#Crie um programa que leia vários números inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre
#quantos números foram digitados e qual foi a soma entre eles (desconsiderando o 999)

contador = 1
parada = 999
soma = 0

while True:

    jogador = int(input("DIGITE UM VALOR DE 0 A 999: "))
    if jogador == parada:      
         print("JOGADOR ENCERRA JOGO")
         break
    else: 
        print("CONTINUE NOVAMENTE: ")
        contador = contador+1
        soma = soma + jogador
        
print(f"A SOMA DOS NUMEROS DIGITADOS É: {soma:.0f} E O NUMERO DE TENTATIVAS FOI : {contador}")  


 
    
    
              



    




