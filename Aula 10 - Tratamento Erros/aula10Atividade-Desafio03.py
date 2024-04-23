# DESAFIO 03

# Escreva um programa que solicite ao usuário para digitar um número inteiro e exiba o resultado da sua raiz quadrada. Lide com o erro caso o número seja negativo.

from math import sqrt
try:
    numero = int(input("Digite um numero inteiro para achar a raiz quadrade : "))
    if numero <0:
            raise ValueError("O numero não pode ser negativo" )
    raiz_quadrada = sqrt(numero)
    print("A raiz quadrada de", numero,"é :", raiz_quadrada)
except ValueError as ve:
    print(ve)
     
                            

