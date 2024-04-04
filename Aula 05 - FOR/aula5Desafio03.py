#DESAFIO 03

#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

total = 0

for elemento in range (1,501, 1):

    if elemento % 2 != 0:
        if elemento % 3 == 0: 
            total = total + elemento
            print(f"A soma entre todos os numeros impares e  multiplos de 3 de 1 a 500 é : {total} ")
            
            
            
            
'''Metodo de correção do exercicio em sala

Soma = 0

for elemento in range (1, 501,1) :
    multiplo3 = elemento % 3
    impar = elemento % 2
    
    if multiplo3 == 0 and impar == 1
    print(f"O muenro {elemento} é impar e multiplo de 3")
    
    soma = soma + elemento
    
else:
    print(f" A soma de todos os valores impares e multiplos de 3 é igual a {soma}")
'''
        
          
          
    