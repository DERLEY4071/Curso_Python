#DESAFIO 07

# Crie um programa que cria uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final mostre a Matriz na tela, com a formatação correta.

matriz = []

for linha in range(3):
    valor = []
    for coluna in range(3):
        valor.append(int(input(f'Informe o valor para [{linha}, {coluna}]: ')))
    matriz.append(valor)

print()
print('-' * 21 + f'\n{"MATRIZ":^22}\n' + '-' * 21)
for linha in range(3):
    for coluna in range(3):
        print(f'|{matriz[linha][coluna]:^5}|', end='')
    print()



# #correção Professor Sila 

# matriz= [[0,0,0],[1,1,1],[2,2,2]]
# c=0

# para i no intervalo (0,3):

# para j em matriz[i]:

# if c==3:
# c=0

# numero= int(input(f"Digite um valor para[{i},{c}]: "))

# matriz[i][c]=numero
# c +=1

# # print(matriz)
# print(matriz[0])
# print(matriz[1])
# print(matriz[2])

# # matriz[0][1] ="joão"
# # print(matriz)


# # print(matriz[0][0])
# # print(matriz[0][1])
# # print(matriz[0][2])