#DESAFIO 01

#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def calculaArea(largura, comprimento):
     area = largura * comprimento        
     print(area)
     
largura = int(input("Digite a largura desejada :  "))
comprimento = int(input("Digite a comprimento desejada :  "))

print(f"O valor da area do terreno é :  ")

calculaArea(largura,comprimento)









