# Desafio 1 

## Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
## da casa, o salário do comprador e em quantos anos ele vai pagar.

## Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

# Casa = 100.000,00
# Salario = 1000,00
# tempo = 5 anos

#Salario
salario = float(input("Digite salario mensal: R$ " ))

#Casa
valorCasa = float(input("Digite valor da casa: R$ " ))

#Tempo para pagar 
anosPagar = int(input("Digite quantos anos para pagar a casa: "))

tempoApagar = anosPagar * 12

percentualSalarial = salario * 0.3 

prestacaoMensal = valorCasa / tempoApagar

if prestacaoMensal > percentualSalarial :
    print(f"A prestação mensal foi de {prestacaoMensal:.2f}, e 30% do seu salario é {percentualSalarial}, protanto seu emprestimo foi negado")
    
else :
    print(f"Parabéns seu emprestimo foi Aprovado")
      












                      