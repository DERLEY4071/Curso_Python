# Explicação sobre importação de Biblioteca com Random com números aleatórios (  Exemplo : import random  )
# Posso renomear a biblioteca e metodos especificos  como from random import randint
# Usando o comando " * " ele importa todos os comandos da Biblioteca 

import random 
from random import randint


nota1 = random.randint(1,10)
nota2 = random.randint(1,10)
media = (nota1 + nota2) / 2

print(f"Digite a primeira nota {nota1}")
print(f"Digite a segunda nota {nota2}")


if media >=7 : 
    print("Aluno Aprovado" )
 
else: 
    print("Aluno Reprovado")  
    



