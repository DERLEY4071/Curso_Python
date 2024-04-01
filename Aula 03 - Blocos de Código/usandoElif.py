## Elif ( É um Comparador de Condições , onde só existira quando tiver um " if "  ou um "else " )    

prova = float(input("Digite a nota na prova do aluno 0 a 70: "))
atividades = float( input("Digite a média das notas das atividades 0 a 30: "))

#Nota prova = 70% da media final
#Nota atividades = 30% da media final

mediaFinal = prova + atividades
print(mediaFinal)

if mediaFinal >= 50 :
    print(f"Aprovado, media final igual a {mediaFinal}")
    
elif mediaFinal >= 40 :
    print(f"Recuperação, media final igual a {mediaFinal}")
    
else:
    print(f"Reprovado, media final igual a {mediaFinal} ")
