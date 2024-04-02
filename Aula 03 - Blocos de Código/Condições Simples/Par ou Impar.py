numero = int(input("Digite um valor: "))

resto = numero % 2 
print(resto)

if resto == 0:
    print ("O valor {numero} é PAR")
else:
    print ("O valor {numero} é IMPAR")