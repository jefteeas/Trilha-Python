import random

num_elementos = random.randint(5, 20)
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

soma_valores = sum(elementos)
media_valores = soma_valores / num_elementos

print("Lista elementos:", elementos)
print("Soma dos valores da lista:", soma_valores)
print("Média dos valores da lista:", round(media_valores, 2))