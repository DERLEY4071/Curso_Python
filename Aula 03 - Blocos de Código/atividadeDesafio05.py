#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

##Condições Necessárias:

##a + b > c

## a + c > b

## b + c > a


retaA = int(input("Digite tamanho reta A: "))

retaB = int(input("Digite tamanho reta B: "))

retaC = int(input("Digite tamanho reta C: "))


somaAB = retaA + retaB

somaAC = retaA + retaC

somaBC = retaB + retaC


if (somaAB > retaC) and (somaAC > retaB) and (somaBC > retaA) :
    print ("Realmente é um triangulo")
    
else:
     print ("Não é um triangulo")



