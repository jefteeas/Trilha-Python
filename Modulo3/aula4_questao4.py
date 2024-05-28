distancia = float(input("Digite a distância da entrega em quilômetros: "))
peso = float(input("Digite o peso do pacote em Kg: "))
valorFrete = 0

if distancia <= 100:
    valorFrete = peso * 1.00
elif 101 <= distancia <= 300:
    valorFrete = peso * 1.50
else:
    valorFrete = peso * 2.00

if peso > 10:
    valorFrete += 10.00

print(f"O valor do frete é: R${valorFrete:.2f}")