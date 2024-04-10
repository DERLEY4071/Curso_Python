#DESAFIO 01

#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.

listaValor = []
valorMaior = valorMenor = posicaoMaior = posicaoMenor = 0



for n in range(1,6):
    valorNumero = int(input("Digite o valor numerico: ")) 
    listaValor.append(valorNumero)
    valorMaior = max(listaValor)
    valorMenor = min(listaValor)
    posicaoMaior = listaValor.index(valorMaior)
    posicaoMenor = listaValor.index(valorMenor)

print(f"O maior valor será :  {valorMaior}  ")
print(f"O menor valor será :{valorMenor}  ")
    
    



