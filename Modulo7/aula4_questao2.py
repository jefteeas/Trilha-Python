import string

caminho_entrada = "./frase.txt"
caminho_saida = "./palavras.txt"

with open(caminho_entrada, "r") as arquivo_entrada:
    conteudo = arquivo_entrada.read()

palavras = [palavra.strip(string.punctuation) for palavra in conteudo.split() if palavra.isalpha()]

with open(caminho_saida, "w") as arquivo_saida:
    arquivo_saida.write("\n".join(palavras))

with open(caminho_saida, "r") as arquivo_saida_leitura:
    conteudo_saida = arquivo_saida_leitura.read()
    print(conteudo_saida)