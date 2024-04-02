#Desafio 5
#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#Equilátero: Todos os lados iguais

#Isósceles: Dois lados iguais

#Escaleno: Todos os lados diferentes

retaA = int(input("Digite tamanho reta A: "))

retaB = int(input("Digite tamanho reta B: "))

retaC = int(input("Digite tamanho reta C: "))


somaAB = retaA + retaB

somaAC = retaA + retaC

somaBC = retaB + retaC


if (somaAB > retaC) and (somaAC > retaB) and (somaBC > retaA) :
    
    if retaA == retaB == retaC:
        print("O Triângulo formando foi o Equilatero")

    elif retaA != retaB != retaC != retaA:
        print("O Triângulo foi o Escaleno")
    
    else:
        print("O Triângulo foi o Isósceles")

       
else:
     print ("Não é um triangulo")
