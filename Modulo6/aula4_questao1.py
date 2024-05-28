pares = [num for num in range(20, 51, 2)]
print("Numeros pares entre 20 e 50:", pares)

quadrados = [num ** 2 for num in [1, 2, 3, 4, 5, 6, 7, 8, 9]]
print("Quadrados dos valores [1, 2, 3, 4, 5, 6, 7, 8, 9]:", quadrados)

divisiveis_por_7 = [num for num in range(1, 101) if num % 7 == 0]
print("Numeros divisiveis por 7 entre 1 e 100:", divisiveis_por_7)

par_impar = ['par' if num % 2 == 0 else 'impar' for num in range(0, 31, 3)]
print("Paridade de valores em range(0,30,3):", par_impar)
