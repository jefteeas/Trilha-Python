frase = input("Digite uma frase: ")

conta_espaco = 0

for caract in frase:
    if caract == ' ':
        conta_espaco += 1

print("Espaços em branco:", conta_espaco)