#Desafio 6

#Crie um programa que faça o computador jogar Jokenpô com você : 

from random import choice

opcoes = ["PEDRA", "PAPEL", "TESOURA"]
escolhaMaquina = choice(opcoes)
print(escolhaMaquina)

escolhaUsuario = input("Informe a sua escolha: ").upper()

if escolhaMaquina == escolhaUsuario:
    print(f"AMBOS ESCOLHERAM {escolhaMaquina}, PORTANTO DEU EMPATE")
    
elif escolhaMaquina == "PEDRA" and escolhaUsuario == "TESOURA" : 
    print(f"A MAQUINA ESCOLHEU {escolhaMaquina}, PORTANTO MAQUINA VENCEU")
    
elif escolhaMaquina == "PAPEL" and escolhaUsuario == "PEDRA" :
    print(f"A MAQUINA ESCOLHEU {escolhaMaquina}, PORTANTO USUARIO VENCEU")
    
elif escolhaMaquina == "TESOURA" and escolhaUsuario == "PAPEL" :
     print(f"A MAQUINA ESCOLHEU {escolhaMaquina}, PORTANTO MAQUINA VENCEU")
     
elif escolhaMaquina == "PEDRA" and escolhaUsuario == "PAPEL" :
     print(f"A MAQUINA ESCOLHEU {escolhaMaquina}, PORTANTO USUARIO VENCEU")
     
elif escolhaMaquina == "PAPEL" and escolhaUsuario == "TESOURA" :
     print(f"VOCÊ ESCOLHEU {escolhaMaquina}, PORTANTO USUARIO VENCEU")
     
elif escolhaMaquina == "TESOURA" and escolhaUsuario == "PEDRA" :
     print(f"A MAQUINA ESCOLHEU {escolhaMaquina}, PORTANTO USUARIO VENCEU")
     
#Else: 
     print(f"A opção esta incorreta ")
     

    
     
     
     
     

    
     
    

