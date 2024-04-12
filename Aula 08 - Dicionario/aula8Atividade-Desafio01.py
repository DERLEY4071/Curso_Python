#DESAFIO 01

#Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No final mostre o conteúdo da estrutura na tela.

dcAluno = {}
notaCorte = 7.0

nome = input("Digite seu nome: ")
media = float(input("Entre com sua média: "))

if(media >= notaCorte):
    dcAluno["Nome"] = nome
    dcAluno["Media"] = media
    dcAluno["Situacao"] = "Aprovado"
else:
    dcAluno["Nome"] = nome
    dcAluno["Media"] = media
    dcAluno["Situacao"] = "Reprovado"
   

print(dcAluno)





#Exercicio resolvido

# aluno = dict()

# aluno['nome'] = input('Informe o nome do aluno(a): ').strip().capitalize()
# aluno['media'] = float(input(f'Informe a média de {aluno["nome"]}: '))

# if aluno['media'] >= 7:
#     aluno['situacao'] = 'Aprovado'
# elif aluno['media'] >= 5:
#     aluno['situacao'] = 'Recuperação'
# else:
#     aluno['situacao'] = 'Reprovado'

# print('-' * 35)
# print(f'NOME: {aluno["nome"]}')
# print(f'MÉDIA: {aluno["media"]}')
# print(f'SITUAÇÃO: {aluno["situacao"]}')



