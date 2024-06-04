import valida
import datetime
import os

def limpaTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')
def criaBarra():
    return print('-' * 32)

data = datetime.datetime.now()
dia = data.day
mes = data.month
ano = data.year

#Funcoes de MENU
def define_menu_gerente():
    while True:

        escolha = menu_gerente()
        if escolha == '1':
            cadastro()
        elif escolha == '2':
            mostraDados()
        elif escolha == '3':
            clientesCadastrados()
        elif escolha == '4':
            cadastroCarros()
        elif escolha == '5':
            carrosCadastrados()
        elif escolha == '6':
            excluir_registro()
        elif escolha == '7':
            editar_registro()
        elif escolha == '8':
            ordenar_carros()
        elif escolha == '0':
            print('\033[1;36m' 'Fim!' '\033[0;0m')
            break
        else:
            limpaTerminal()
            criaBarra()
            print('\033[1;31m''Insira uma opcao valida!''\033[0;0m')
            criaBarra()

def define_menu_funcionario():
    while True:

        escolha = menu_funcionario()
        if escolha == '1':
            cadastro()
        elif escolha == '2':
            clientesCadastrados()
        elif escolha == '3':
            cadastroCarros()
        elif escolha == '4':
            carrosCadastrados()
        elif escolha == '5':
            ordenar_carros()
        elif escolha == '0':
            print('\033[1;36m' 'Fim!' '\033[0;0m')
            break
        else:
            limpaTerminal()
            criaBarra()
            print('\033[1;31m''Insira uma opcao valida!''\033[0;0m')
            criaBarra()

def menu_funcionario():
    print('====== <<< ''\033[1;96m''LOCADORA''\033[0;0m'' >>> ======')
    print('|  [''\033[1;36m''1''\033[0;0m''] Cadastrar Cliente     |')
    print('|  [''\033[1;36m''2''\033[0;0m''] Mostrar Clientes      |')
    print('|  [''\033[1;36m''3''\033[0;0m''] Cadastrar Carro       |')
    print('|  [''\033[1;36m''4''\033[0;0m''] Mostrar Carros        |')
    print('|  [''\033[1;36m''5''\033[0;0m''] Ordenar Carros        |')
    print('|  [''\033[1;36m''0''\033[0;0m''] Sair                  |')
    print('------------------------------')
    x = input('\033[1;36' 'IInsira a Opcao: ''\033[0;0m')
    print('------------------------------')
    return x

def menu_gerente():
    print('====== <<< ''\033[1;96m''LOCADORA''\033[0;0m'' >>> ======')
    print('|  [''\033[1;36m''1''\033[0;0m''] Cadastrar Cliente     |')
    print('|  [''\033[1;36m''2''\033[0;0m''] Dados do Cliente      |')
    print('|  [''\033[1;36m''3''\033[0;0m''] Mostrar Clientes      |')
    print('|  [''\033[1;36m''4''\033[0;0m''] Cadastrar Carro       |')
    print('|  [''\033[1;36m''5''\033[0;0m''] Mostrar Carros        |')
    print('|  [''\033[1;36m''6''\033[0;0m''] Excluir Registros     |')
    print('|  [''\033[1;36m''7''\033[0;0m''] Editar Registros      |')
    print('|  [''\033[1;36m''8''\033[0;0m''] Ordenar Carros        |')
    print('|  [''\033[1;36m''0''\033[0;0m''] Sair                  |')
    print('------------------------------')
    x = input('\033[1;36' 'IInsira a Opcao: ''\033[0;0m')
    print('------------------------------')
    return x
#Fim das funcoes de MENU


# funcao para editar registros (menu)
def editar_registro():
    arquivo = input("Qual registro gostaria de alterar? (logins ou carros): ")
    if arquivo == 'logins':
            editar_logins()
    elif arquivo == 'carros':
            editar_carros()
    else:
        print('Entrada invalida, digite apenas "logins" ou "carros"')


#Editar Logins
def editar_logins():
    with open('logins.txt', 'r') as arquivo:
        nome_antigo = input("Qual o registro gostaria de alterar?(Digite o nome, senha, funcao, email ou telefone): ")
        nome_novo = input("Digite o novo registro: ")
        
        linhas = arquivo.readlines()
    
    # Editar a informação desejada em cada linha
        linhas_editadas = [linha.replace(nome_antigo, nome_novo) if nome_antigo in linha else linha for linha in linhas]
    
    # Escrever as linhas de volta no arquivo
    with open('logins.txt', 'w') as arquivo:
        arquivo.writelines(linhas_editadas)
       
#Editar Carros
def editar_carros():
    with open('carros.txt', 'r') as arquivo:
        nome_antigo = input("Qual o registro gostaria de alterar?(Digite o nome, placa ou valor): ")
        nome_novo = input("Digite o novo registro: ")
        
        linhas = arquivo.readlines()
    
    # Editar a informação desejada em cada linha
        linhas_editadas = [linha.replace(nome_antigo, nome_novo) if nome_antigo in linha else linha for linha in linhas]
    
    # Escrever as linhas de volta no arquivo
    with open('carros.txt', 'w') as arquivo:
        arquivo.writelines(linhas_editadas)


# Funcao de Login
def loginCliente():
    limpaTerminal()
    print('====== < ''\033[1;92m''Login''\033[0;0m'' > ======')
    criaBarra()
    userlogin = input('Login: ')
    usersenha = input('Senha: ')
    usergerente = '2'
    userfuncionario = '1'

    valida = False
    logins = open('logins.txt', 'r')
    for linha in logins.readlines():
        valores = linha.split('-')
        if userlogin == valores[0].split(':')[1].strip() and usersenha in valores[1].split(':')[1].strip() and usergerente in valores[2].split(':')[1].strip():
            limpaTerminal()
            criaBarra()
            print('\033[1;32m''Gerente logado''\033[0;0m')
            criaBarra()
            define_menu_gerente()

        elif userlogin == valores[0].split(':')[1].strip() and usersenha in valores[1].split(':')[1].strip() and userfuncionario in valores[2].split(':')[1].strip():
            limpaTerminal()
            criaBarra()
            print('\033[1;32m''Funcionario logado''\033[0;0m')
            criaBarra()
            define_menu_funcionario()
        
#Cadastro, checar login, adicionar dados no txt
def cadastro():
    limpaTerminal()
    print('====== < ''\033[1;92m''Cadastrar Usuario: ''\033[0;0m'' > ======')
    login = valida.Login()

    #Verifica se ja existe o login cadastrado
    lerlogins = open('logins.txt','r')
    for linha in lerlogins.readlines(): #lê as linhas do arquivo logins.txt
        valores = linha.split('-')
        #Cria a lista com os valores
        if login == valores[1].split(':')[1].strip():
            #Confere o login cadastrado
            limpaTerminal()
            criaBarra()
            print('\033[1;31m''Login ja existente''\033[0;0m')
            criaBarra()
            return
    lerlogins.close()

    senha = valida.Senha()
    funcao = valida.funcao()
    email = valida.Email()
    data = valida.Data()
    tele = valida.tele()

    limpaTerminal()
    criaBarra()
    print('\033[1;32m''Cliente Cadastrado com Sucesso!''\033[0;0m')
    criaBarra()

    #Adiciona os dados no banco login.txt
    logins = open("logins.txt", 'a')
    logins.write(f'Login: {login} -Senha: {senha} -Funcao: {funcao} -Email: {email} -Data de Nascimento: {data} -Numero de celular: {tele} \n')
    logins.close()
    return

#Cadastrar carros, adicionar dados no txt
def cadastroCarros():
    limpaTerminal()
    print('====== < ''\033[1;92m''Cadastrar Carro: ''\033[0;0m'' > ======')
    nome = valida.nomeCarros()
    placa = valida.placa()
    valor = valida.valorCarro()

    #Verifica se ja existe o carro cadastrado
    lercarros = open('carros.txt','r')
    for linha in lercarros.readlines(): #lê as linhas do arquivo carros.txt
        valores = linha.split('-')
        #Cria a lista com os valores
        if nome == valores[0].split(':')[1].strip() and valores[1].split(':')[1].strip():
        #Confere o carro cadastrado
            limpaTerminal()
            criaBarra()
            print('\033[1;31m''Carro ja existente''\033[0;0m')
            criaBarra()
            return
    lercarros.close()

    limpaTerminal()
    criaBarra()
    print('\033[1;32m''Carro Cadastrado com Sucesso!''\033[0;0m')
    criaBarra()

    #Adiciona os dados no banco login.txt
    carros = open("carros.txt", 'a')
    carros.write(f'Nome: {nome} -Placa: {placa} -Valor: {valor} \n')
    carros.close()
    return

#excluir arquivos no txt
def excluir_registro():
    # Solicitar ao usuário o nome do arquivo e o registro a ser excluído
    arquivo = input("Digite o nome do arquivo(logins ou carros): ")
    if arquivo == 'logins':
        registro = input("Digite o registro a ser excluído(nome): ") 
        with open('logins.txt', 'r') as file:
            lines = file.readlines()
        for line in lines:
            if registro in line:
                lines.remove(line)

        with open('logins.txt', 'w') as file:
            for line in lines:
                file.write(line)

    elif arquivo == 'carros':
        registro = input("Digite o registro a ser excluído(nome): ") 
        with open('carros.txt', 'r') as file:
            lines = file.readlines()
        for line in lines:
            if registro in line:
                lines.remove(line)

        with open('carros.txt', 'w') as file:
            for line in lines:
                file.write(line)

    else:
        print('Opcao Invalida, apenas "logins" ou "carros".')
                


#mostrar dados de usuario
def mostraDados():
    limpaTerminal()
    print('====== < ''\033[1;92m''Login''\033[0;0m'' > ======')
    criaBarra()
    userlogin = input('Login: ')

    logins = open('logins.txt', 'r')
    
    for linha in logins.readlines():
        valores = linha.split('-')
        if userlogin == valores[0].split(':')[1].strip():
            limpaTerminal()
            criaBarra()
            for percorre in range(len(valores)):
                print(valores[percorre])

            criaBarra()
            logins.close()
            break

#exibir dados de todos ja cadastrados
def clientesCadastrados():
    limpaTerminal()
    print('====== < ''\033[1;92m''Clientes cadastrados''\033[0;0m'' > ======')
    logins = open('logins.txt', 'r')
    for linha in logins.readlines():
        l = linha.split('-')
        print('\033[1;92m'f'{l[0]} | {l[2]}''\033[0;0m')
    criaBarra()
    return

#exibir carros cadastrados
def carrosCadastrados():
    limpaTerminal()
    print('====== < ''\033[1;92m''Carros cadastrados''\033[0;0m'' > ======')
    carros = open('carros.txt', 'r')
    for linha in carros.readlines():
        l = linha.split('-')
        print('\033[1;92m'f'{l[0]} | {l[1]} | {l[2]}''\033[0;0m')
    criaBarra()
    return
            
#Ordena os carros em ordem crescente ou decrescente de valores
def ordenar_carros():
    # Nome do arquivo .txt contendo os dados dos carros
    arquivo_nome = 'carros.txt'
    
    # Lista para armazenar os dados dos carros
    carros = []

    # Abrir e ler o arquivo
    with open(arquivo_nome, 'r') as arquivo:
        linhas = arquivo.readlines()
        
        for linha in linhas:
            try:
                nome, placa, valor = linha.strip().split('-')
                # Remover "Valor: " e espaços em branco
                valor = valor.replace("Valor: ", "").strip()
                # Remover pontos e substituir vírgula por ponto para o formato brasileiro
                valor = valor.replace('.', '').replace(',', '.')
                valor = float(valor)
                carros.append({'nome': nome, 'placa': placa, 'valor': valor})
            except ValueError:
                continue

    ordem = input("Deseja ordenar os carros em ordem crescente ou decrescente? (c/d): ").strip().lower()
    
    # Ordenando a lista de carros
    if ordem == 'c':
        carros_ordenados = sorted(carros, key=lambda x: x['valor'])
    elif ordem == 'd':
        carros_ordenados = sorted(carros, key=lambda x: x['valor'], reverse=True)
    else:
        print("Opção inválida! Ordenando por padrão em ordem crescente.")
        carros_ordenados = sorted(carros, key=lambda x: x['valor'])
    
    # Imprime os carros ordenados
    for carro in carros_ordenados:
        print(f"{carro['nome']}, {carro['placa']}, Valor: {carro['valor']:.2f}")







