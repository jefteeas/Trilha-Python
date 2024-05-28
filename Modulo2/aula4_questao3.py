# Cria uma funcao para cadastrar os produtos
def produtos(numero):
    nome = input(f"Digite o nome do produto {numero}: ")
    preco = float(input(f"Digite o preço do produto {numero}: "))
    quantidade = int(input(f"Digite a quantidade {numero}: "))
    return preco * quantidade

produto1 = produtos(1)
produto2 = produtos(2)
produto3 = produtos(3)

# Calcula o preço total
pt = produto1 + produto2 + produto3

# Imprime o resultado
print(f"Total: R${pt:,.2f}")