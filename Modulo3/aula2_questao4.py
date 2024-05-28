classe = input("Escolha a classe: ")

forca = int(input("Digite os pontos de força: "))
magia = int(input("Digite os pontos de magia: "))

validacao = False

if classe == "guerreiro":
    validacao = forca >= 15 and magia <= 10
elif classe == "mago":
    validacao = forca <= 10 and magia >= 15
elif classe == "arqueiro":
    validacao = 5 < forca <= 15 and 5 < magia <= 15

print(f"Pontos de atributo consistentes com a classe escolhida: {validacao}")