#DESAFIO 03

#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro Serie B de Futebol, na ordem de colocação. Depois mostre:

#A) Apenas os 5 primeiros colocados.

#B) Os últimos 4 colocados da tabela.

#C) Uma lista com os times em ordem alfabética.

#D) Em que posição na tabela está o time do Santos.

timeserieB = ("Santos","Mirassol","Avaí","Paissandu","Goias","Ceará","America-MG","Coritiba","Brusque","Ponte Preta","CRB","Novorizontino","Ituano","Amazonas","Guarani","Vila Nova","Botafogo-SP","Operário","Sport","Chapecoense")
time_alfabetica = sorted(timeserieB)

print(f"A) Apenas os 5 primeiros colocados: {timeserieB[0:5]}")

print(f"B) Os últimos 4 colocados da tabela: {timeserieB[-4:]} ")

print(f"C) Uma lista com os times em ordem alfabética:{time_alfabetica}")

posicaoSantos = timeserieB.index("Santos")
print(f"D) Em que posição na tabela está o time do Santos: {posicaoSantos +1}°")




'''Outra Forma 
tabelaBrasileirao = ("Santos","Mirassol","Avaí","Paissandu","Goias","Ceará","America-MG","Coritiba","Brusque","Ponte Preta","CRB","Novorizontino","Ituano","Amazonas","Guarani","Vila Nova","Botafogo-SP","Operário","Sport","Chapecoense")
top5 = tabelaBrasileirao [0:5]
ultimos4 = tabelaBrasileirao [-4:]
ordemAlfabetica = sorted(tabelaBrasileirao)

print(f"A) Apenas os 5 primeiros colocados: {tabelaBrasileirao[0:5]}")

print(f"B) Os últimos 4 colocados da tabela: {tabelaBrasileirao[-4:]} ")

print(f"C) Uma lista com os times em ordem alfabética:{ordemAlfabetica}")

posicaoSantos = timeserieB.index("Santos")
print(f"D) Em que posição na tabela está o time do Santos:{posicaoSantos + 1}")'''
