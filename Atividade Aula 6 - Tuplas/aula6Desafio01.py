#DESAFIO 01

#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.


numerosExtenso = ("Zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete","oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    escolhaNumero = int(input("Digite numero a escolher de 0 a 20:"))
    
    if escolhaNumero>=0 and escolhaNumero <=20:
        break
    
    print("Tente novamente")
    
print(f"Voce digitou o numero : {escolhaNumero}, {numerosExtenso[escolhaNumero]}")




