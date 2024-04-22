try:
    with open ("data.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("O Arquivo não Existe")
except ZeroDivisionError:
    print("IMpossivel dividir um numero por zero ")
finally:
    print("FIM")
   