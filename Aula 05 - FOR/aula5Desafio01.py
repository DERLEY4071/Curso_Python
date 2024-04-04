#DESAFIO 01

#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
# Comentario sobre "Time" =  (roda programa no tempo solicitado ) / "Time.Sleep" = ( roda programa como se fosse um relogio comparador  de tempo)

import time

for contagemRegressiva in range (10,-1,-1):
     print(contagemRegressiva)
     time.sleep(1)
     
else:
     
     print("Estouro de fogos e Artificios")




