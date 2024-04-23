# DESAFIO 04
# 






try:
    while True:
        nome = input("Digite seu nome.: ")
        idade = input ("Digite sua idade.: ")

        idade = int(idade)
        break
 
 
except ValueError:
    print("Idade invalida, por favor digite um numero inteiro.\n")
    mensagem_personalizada =  (f"Ola {nome}, você tem {idade} anos")
    print(mensagem_personalizada)
    
        
    
