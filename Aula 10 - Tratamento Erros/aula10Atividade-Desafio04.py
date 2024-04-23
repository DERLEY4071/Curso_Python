# DESAFIO 04
# Escreva um programa que peça ao usuário para digitar seu nome e idade. Em seguida, exiba uma mensagem personalizada que inclua o nome e a idade. Lide com o erro caso a idade digitada não seja um número.


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
    
    
 # Correçao Pedro       
    
# try:
    
#     nome = input("Digite seu nome.: ")
#     idade = input ("Digite sua idade.: ")
        
# except ValueError:
#     print("Digite sua idade com valor numerico : ")
    
# else:
#      print(f"Cadastro concluido")
      
   
