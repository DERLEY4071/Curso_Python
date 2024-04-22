# DESAFIO 01

# Escreva um programa que peça ao usuário para digitar dois
# números e divida o primeiro número pelo segundo. Certifique-se
# de lidar com a possibilidade de divisão por zero.

try:
        n1 = int(input("Digite primeiro numero : "))
        n2 = int(input("Digite segundo numero : "))
        
        divisao = n1/n2 
        print(divisao)
except ZeroDivisionError:
    print("Não Existe Divisão por ZEro")
        
    
