#DESAFIO 06

#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
# função "end" para fazer junção ou concatenar os prints usados no programa de acordo com a quantidade de junção, menos a ultima

primeiroTermo = int(input("DIGITE O PRIMEIRO TERMO:"))
razao = int(input("DIGITE A RAZAO:"))


ultimoTermo = (primeiroTermo + (10 - 1) * razao) + razao

for elemento in range (primeiroTermo, ultimoTermo, razao):
    print(elemento, end='->')
    
else:
    print("FIM")
    


