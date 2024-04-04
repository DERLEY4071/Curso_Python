#DESAFIO 05

#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar desconsidere-o.

total = 0

for n1 in range (1,7):
    numero = int(input(f"Digite {n1}º numero: "))
    if numero % 2 == 0:  
        total = total + numero
        #print(f"{n1}")
else:
    print(f"A soma dos numeros pares é : {total}")
    
    
    


'''Metodo de correção do exercicio em sala

soma = 0

for elemento in range (1,7):
    numero = int(input("DIGITE UM VALOR"))

resto = numero %2

if resto == 0:
    soma = soma + numero   
    
else: 
    print(f"A soma dos valores pares digitados foi igual a {soma}")
'''

