#Desafio01
## Escreva um programa que faça o computador “pensar” em um
## número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
## qual foi o número escolhido pelo computador.

import random   

numero1 = random.randint(0,5)

numero2 = int(input("Digite um numero de 0 a 5: "))

if numero1 == numero2 : 
    print("Você acertou o numero que a máquina escolheu" )
    
else:    
    print("Você errou o numero que a máquina escolheu" )
    print(f"A máquina escoulheu {numero1}" )





