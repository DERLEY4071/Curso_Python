#Desafio01
## Escreva um programa que faça o computador “pensar” em um
## número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
## qual foi o número escolhido pelo computador.

import random   

numeroMaquina = random.randint(0,5)

numeroUsuario = int(input("Digite um numero de 0 a 5: "))

if numeroMaquina == numeroUsuario : 
    print(f"O número sorteado foi {numeroMaquina} parabéns foi acertou" )
    
else:    
    print(f"O número sorteado foi {numeroMaquina} então você errou , tente novamente " )
   





