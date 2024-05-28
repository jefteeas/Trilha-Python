#Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17). 
#Escreva um programa que solicite as idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos, 
#indicando que podem entrar no bar, e False caso contrário.

idade_juliana = int(input("Qual a idade de Juliana?"))
idade_cris = int(input("Qual a idade de cris?"))

permitir = idade_juliana >= 18 and idade_cris >= 18
print (permitir)
