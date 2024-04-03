
from random import *
escolhaMaquina = randint(1,20)
print(escolhaMaquina)

for elemento in range (1,11,1):
    escolhaUsuario = int(input(f"{elemento}° Rodada , DIGITE UM NUMERO:"))
    
    if escolhaUsuario == escolhaMaquina:
       print("Usuario Venceu")
       break
else:
    print("Maquina Venceu")
    
print("Acabou o jogo")
        
    
    
    





     
        