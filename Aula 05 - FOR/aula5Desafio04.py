#DESAFIO 04

#Refaça o DESAFIO 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

usuarioEscolhe = float(input("Digite numero a escolher:"))
#Na condição acima posso usar o "float" ou Int"

for elemento in range (1, 11) :
    print(f"{usuarioEscolhe} x {elemento} = {usuarioEscolhe * elemento}")





'''Metodo de correção do exercicio em sala
for elemento in range (1,11)
resultado = elemento * numero
print(f"{numero} * {elemento} = {resultado}")
'''