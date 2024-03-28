##Desenvolva um programa que pergunte a distância de uma
##viagem em Km. Calcule o preço da passagem cobrando R$
## 0,50 por Km para viagens de até 200 Km e R$ 0,45 para viagens mais longas

distancia1 = int(input("Digite a dsitancia de sua viagem em Km: "))

p1 = (0.50 * distancia1)
p2 = (0.45 * distancia1)


if distancia1 <= 200 :
    print(f"Você esta fazendo uma viagem curta, portanto sua passagem é R$ {p1} " )
    
else: 
    print(f"Você esta fazendo uma viagem mais longa, portanto sua passagem é R$ {p2} " )    
