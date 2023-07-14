nota = input("digite a sua nota:")

nota = int(nota)


print(nota)
if nota <= 4:
    print("Reprovado")
elif nota >4 and nota <=6:
    print("Recuperação")
else:
    print("Aprovado")
    
