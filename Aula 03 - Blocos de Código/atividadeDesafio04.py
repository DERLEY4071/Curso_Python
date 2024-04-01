#Faça um programa que leia três números e mostre qual é o maior e qual é o menor
# And - Or  = Comparação ( And - duas condições tem que ser verdadeira /  Or - Apenas uma condição pode ser verdadeira )

num1= int(input("Digite o primeira valor: " ))
num2= int(input("Digite o segundo valor:" ))
num3= int(input("Digite o terceiro valor: " ))


if num1 > num2 and num1 > num3 :
    print(F"Maior numero é o {num1}")
    
if num2 > num3 and num2 > num1 :
     print(F"Maior numero é o {num2}")  
     
if num3> num1 and num3 > num2 : 
     print(F"Maior numero é o {num3}")     
     
if num1 < num2 and num1 < num3 :
    print(F"Menor numero é o {num1}") 
    
if num2 < num1 and num2 < num3 :
     print(F"Menor numero é o {num2}")  

if num3 < num1 and num3 < num2 :
     print(F"Menor numero é o {num3}")  
     
       
    
    
    
