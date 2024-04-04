#Desafio 02

#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for elemento in range (1, 51):
   if elemento % 2 == 0:
       print(f"O numero {elemento} é par")
   



'''Metodo de correção do exercicio em sala 

for elemento in range (1, 50, 1):
    
    resto = elemento % 2
    
    if resto == 0:
       # print(f"O numero {elemento} é par")
'''