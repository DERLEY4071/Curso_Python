#Faça um programa que leia três números e mostre qual é o maior e qual é o menor
# And - Or  = Comparação ( And - duas condições tem que ser verdadeira /  Or - Apenas uma condição pode ser verdadeira )

batata = input("Você comprou a batata [S/N] :").upper()
maionese = input("Você comprou a maionese [S/N] :").upper()

if batata == "S" and maionese == "S" :     
    print ("TEM MAIONESE")
    
else:
    print ("NÃO TEM SALADA DE MAIONESE")


