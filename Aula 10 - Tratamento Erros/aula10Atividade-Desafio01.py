# DESAFIO 01

# Escreva um programa que peça ao usuário para digitar dois
# números e divida o primeiro número pelo segundo. Certifique-se
# de lidar com a possibilidade de divisão por zero.

while True:

    try:
        n1 = int(input("Digite primeiro numero : "))
        n2 = int(input("Digite segundo numero : "))
                
        divisao = n1/n2 
        print(divisao)
    except ZeroDivisionError:
                
        print("Não Existe Divisão por ZEro")
        
    except ValueError:
        
        print("DIGITE VALOR NUMERICO")

    else:
        print(f" O Valor da divisão foi : {divisao} ")
        break        
         
