#DESAFIO 01

#Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No final mostre o conteúdo da estrutura na tela.

meuDicionario = {}

meuDicionario['nome'] = str(input('Digite seu nome : ')).upper()
meuDicionario['nota'] = float(input('Digite sua nota : '))

print(meuDicionario)

if meuDicionario["nota"]>=7:
    meuDicionario["Situação"] = "Aprovado"
    
elif meuDicionario["nota"]>=5 and meuDicionario ["nota"]<=7:
    meuDicionario ["Situação"] = "Recuperação - Tem Salvação"
     
else:
    meuDicionario["Situação"] = "Reprovado - Se Lascou"
    
# for k, v in meuDicionario.items() :
#     print(f"O {k} é igual a : {v}")    
    
print(meuDicionario)
print(f"O nome é igual a {meuDicionario["nome"]}" )
print(f"A Média é igual a {meuDicionario['nota']}")
print(f"Sua Situação é {meuDicionario['situacao']}")

   
    

#Exercicio resolvido

# dcAluno = {}
# notaCorte = 7.0

# nome = input("Digite seu nome: ")
# media = float(input("Entre com sua média: "))

# if(media >= notaCorte):
#     dcAluno["Nome"] = nome
#     dcAluno["Media"] = media
#     dcAluno["Situacao"] = "Aprovado"
# else:
#     dcAluno["Nome"] = nome
#     dcAluno["Media"] = media
#     dcAluno["Situacao"] = "Reprovado"
   

# print(dcAluno)







