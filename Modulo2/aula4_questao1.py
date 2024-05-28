#Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura),
#bem como o preço do metro quadrado da região em ponto flutuante. 
#Calcule o valor do terreno e imprima o resultado com a formatação apresentada a seguir.
#O terreno possui 250m2 e custa R$512,490.50
#Comente na linha acima de cada instrução uma breve descrição da instrução.

#Fórmulas:
#area_m2 = comprimento * largura
#preco_total = preco_m2 * area_m2


# comprimento do terreno em metros
comprimento = int(input("Digite o comprimento do terreno (em metros): "))

# largura do terreno em metros
largura = int(input("Digite a largura do terreno (em metros): "))

# preço do metro quadrado
preco_m2 = float(input("Digite o preço do metro quadrado (em R$): "))

# Calcula a área do terreno em metros quadrados
area_m2 = comprimento * largura

# Calcula o preço total do terreno
preco_total = preco_m2 * area_m2

# Imprime o resultado
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")

