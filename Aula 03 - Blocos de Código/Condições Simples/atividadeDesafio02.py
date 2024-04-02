## Escreva um programa que leia a velocidade de um carro.
## Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
## ele foi multado, a multa vai custar R$ 7,00 por cada Km acima do limite.

import random 

n1 = int(input("Digite a velocidade do carro: "))
n2 = 80
fmulta = (n1-80) * 7



if n1 <= 80 :
    print(F"Você é um motorista Consciente: " )
    
else: 
    print(f"Você esta acima do limite e foi multado em R$ {fmulta},00 : " )    


