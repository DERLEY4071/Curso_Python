#DESAFIO 03

#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na sua posição
#correta de inserção (sem usar o sort()).No final mostre a lista ordenada na tela

lista = []

for n in range (0,5):
   escolhaNumero = int(input("Digite numero a escolher de 0 a 5:  "))
   
   if n == 0 or escolhaNumero > lista[-1]:
       lista.append(escolhaNumero)
       print("Adicionado ao final da lista" )
       
   else:
       pos = 0
       while pos < len(lista):
           if escolhaNumero <= lista[pos]:
               lista.insert(pos,escolhaNumero)
               print(f"Adicionado na posição {pos} da lista :")
               break
           pos +=1
           
               
           
print(f"Os valores digitados em ordem crescentes foram : {lista}")            
            
                        
   
   


