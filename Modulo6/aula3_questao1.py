numeros = []

print("Digite pelo menos 4 números inteiros. Digite 'fim' para terminar.")

while True:
    entrada = input("Digite um número (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        if len(numeros) >= 4:
            break
        else:
            print("Por favor, digite pelo menos 4 números.")
            continue
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print("Lista original:", numeros)
print("Os 3 primeiros elementos:", numeros[:3])
print("Os 2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])