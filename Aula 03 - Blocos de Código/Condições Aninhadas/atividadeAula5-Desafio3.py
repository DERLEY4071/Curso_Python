#Desafio 3

#Crie um programa que leia duas notas entre 0 a 10 de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida

#Média abaixo de 5.0: REPROVADO

#Média entre 5.0 a 6.9: RECUPERAÇÃO

#Média igual ou superior a 7.0: APROVADO

nota1 = float(input("Digite a primeira nota de 0 a 10: "))
nota2 = float(input("Digite a segunda nota  de 0 a 10: "))

if nota1 >=0 and nota1 <=10 and nota2 >=0 and nota2 <=10:


    media =  (nota1 + nota2) / 2
    print(f"Sua media é: {media} ")

    n = 5
    nf = 6.9
    m = 7 


    if media >=7 :
        print(f"A sua media foi de {media} , portanto: Aluno Aprovado")
        
    elif media >= 5 :
        print(f"A sua media foi de {media} , portanto: Aluno em Recuperação") 
        
    else:
        print(f"A sua media foi de {media}, portanto:Aluno Reprovado")
     
else :
    print("Por favor nos informar uma nota valida")
     
    





          