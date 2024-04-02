#Desafio 4
##A confederação Nacional de Natação precisa de uma programa que leia o ano de nascimento de uma atleta e mostre sua categoria, de acordo com a idade.

#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 24 anos: SÊNIOR
#Acima: MASTER

from datetime import *

dataAtual = date.today()
anoAtual = dataAtual.year

print(anoAtual)


anoNascimento = int(input("Digite o ano de nascimento do atleta: "))
    
idade = anoAtual - anoNascimento 

if anoNascimento <=9 :
    print ("O atleta se enquadra na categoria : Mirim")
    
elif idade <= 14 :
    print ("O atleta se enquadra na categoria : Infantil")
    
elif idade <= 19 :
    print ("O atleta se enquadra na categoria : Junior")
    
elif idade <=24 :
    print ("O atleta se enquadra na categoria : Sênior")
    
else :
    print ("O atleta se enquadra na categoria : Master")

