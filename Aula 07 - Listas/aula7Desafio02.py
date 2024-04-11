#DESAFIO 02

#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
#No final serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
    numero = str(input("digite um valor para adicionar em uma lista e N para parar: " ))
    
    if numero.upper() == "N": 
        break
    
    if int(numero) in lista:
        print(f"O numero {int(numero)} ja foi adicionado ")
        
    else:
        lista.append(int(numero))
        
lista.sort()
print(f"Os valores digitados em ordem crescentes foram : {lista}")
        