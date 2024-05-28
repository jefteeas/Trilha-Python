n = int(input("Digite a quantidade de respondentes: "))
soma_idades = 0
contador = 0

while contador < n:
    idade = int(input(f"Digite a idade do respondente {contador + 1}: "))
    soma_idades += idade
    contador += 1

media_idades = soma_idades / n

print(f"A média de idade dos respondentes é: {media_idades:.2f}")