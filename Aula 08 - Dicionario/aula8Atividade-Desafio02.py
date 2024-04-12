#DESAFIO 02

# Crie um programa onde 4 jogadores joguem um dado e tenham resultado aleatórios. Guarde esses resultados em um
# dicionário .
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior numero no dado.

from random import randint
from time import sleep
from operator import itemgetter

meuDicionario = {
    "jogador1" : randint(1,6),
    "jogador2" : randint(1,6),
    "jogador3" : randint(1,6),
    "jogador4" : randint(1,6)
    
   }

for k, v in meuDicionario.items() :
    print(f"{k} tirou {v} no dado") 
    sleep(1)
    
    # print("Em ordem Cresecente : ")    
    # sorted(iterable, key=key, reverse==reverse)
    # sorted(Quem?, qual a chave , quem inverte)  
    
    print('-' * 24)
    
ranking = sorted(meuDicionario.items(),key=itemgetter(1), reverse=True)
print(ranking)
    

      



#Outra Forma :

# from random import randint

# players = dict()
# dado = 0

# print("Valores sorteados: \n")

# for i in range(4):
#     jogada = randint(1, 6)
#     players[f"jogador {i + 1}"] = jogada

#     print(f"O jogador {i + 1} tirou {jogada} pontos no dado.")
    
#     print('-' * 35)

# print("\nRanking dos jogadores:")
# players_list = sorted( 
#     list(zip(players.values(), players.keys())), reverse=True)


# for i, player in enumerate(players_list):
#     print(
#         f"{i+1}º lugar: {players_list[i][1]} com {players_list[i][0]} pontos")
#     dado += 1