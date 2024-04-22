# DESAFIO 03

# Faça um programa que tenha uma função chamada maior(), que receba três parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é
# o maior.

n1 = int(input("Digite o primeiro valor : "))
n2 = int(input("Digite o segundo valor : "))
n3 = int(input("Digite o terceiro valor : "))

def maior(numero1, numero2, numero3 ):
    if numero1 > numero2 and numero1 > numero3:
        return f" O numero {numero1} foi o maior valor"
    
    elif numero2 > numero3 :
       return f" O numero {numero2} foi o maior valor"
    else:
         return f" O numero {numero3} foi o maior valor"

print(maior(n1,n2,n3))
        

