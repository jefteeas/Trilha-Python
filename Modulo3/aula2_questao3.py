idade = int(input("Qual a sua idade?"))
qjogos = int(input("Quantos jogos de tabuleiro ja jogou?"))
qvenceu = int(input("quantos jogos ja venceu?"))

permitido = (idade >= 16 and idade <= 18) and (qjogos >= 3) and qvenceu >= 1
print (f"Apto para entrar no clube: {permitido}")
