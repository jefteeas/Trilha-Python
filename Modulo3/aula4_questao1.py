#Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. 
#Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar. 
#Lembre-se do operador do python % que retorna o resto de uma divisão.

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))
soma = numero1 + numero2
if soma % 2 == 0:
    resultado = "PAR"
    print (f"Esse numero e {resultado}")
else:
    resultado = "IMPAR"
    print (f"Esse numero e {resultado}")