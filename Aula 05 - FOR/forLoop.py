#forLoop

from random import *

maquina = usuario = 0


for elemento in range (1,10,1):
    
    escolhaMaquina = randint(0,5)
    escolhaUsuario = int(input(f"{elemento}° Rodada , DIGITE UM NUMERO:"))
    
    if escolhaMaquina == escolhaUsuario :
      # usuario = usuario + 1 ( podemos usar das duas formas )
        usuario +=1
        print("USUARIO VENCEU A RODADA")       
    else:
        maquina = maquina + 1
        print("MAQUINA VENCEU A RODADA")
else:          
    if usuario > maquina :
           print(f"Você acertou{usuario}, portanto você venceu")
       
    else:
        print(f"A maquina fez{maquina} pontos, portantoa maquina venceu")
