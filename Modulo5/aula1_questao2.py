import random
import math

n = int(input("Digite a quantidade de valores aleatórios a serem gerados: "))

soma = 0
for _ in range(n):
    valor_aleatorio = random.randint(0, 100)
    soma += valor_aleatorio
    print(f"{soma}")

raiz_quadrada = math.sqrt(soma)
print(f"A raiz quadrada da soma dos {n} valores inteiros aleatórios é: {raiz_quadrada:.2f}")