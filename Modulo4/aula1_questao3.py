n1 = int(input("Digite a nota: "))
n2 = int(input("Digite a nota: "))
n3 = int(input("Digite a nota: "))
media = (n1+n2+n3)/3

if media >= 60:
    print ("Aprovado")
elif media >= 40 and media < 60:
    print ("Recuperacao")
else:
    print("Reprovado")
    print("FIM")