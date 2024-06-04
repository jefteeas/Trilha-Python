import defs

def nomeCarros():
    while True:
        nome = input('Nome: ')
        if nome == '':
            print('Error! Entrada Vazia!')
            continue
        temp = ''.join(nome.split(' '))
        for i in temp:
            if i.isdigit():
                print ('Digite um nome valido.')
                break
        else:
            return nome.strip(' ')
        
def placa():
    while True:
        placa = input('Placa: ')
        if placa == '':
            print('Error! Entrada Vazia!')
            continue
        return placa.strip(' ')
        
def Senha():
    while True:
        senha = input('Senha: ')
        if senha == '':
            print('Error! Entrada Vazia!')
            continue
        return senha.strip(' ')
    
def valorCarro():
    while True:
        valor = input('Valor do Aluguel: ')
        if valor == '':
            print('Error! Entrada Vazia!')
            continue
        return valor.strip(' ')
    
def Email():
    while True:
        email = input('Email: ')
        if email == '':
            print('Error! Entrada Vazia!')
        elif '@' and '.com' in email:
            return email.strip(' ')
        else: 
            print('Email Invalido! Deve conter "@" e ".com"')

def Data():
    while True:
        data = input('Nascimento (dd/mm/aaaa): ')
        if data == '':
            print ('Error! Entrada Invalida.')
            continue
        temp = ''.join(data.split('/'))
        if not temp.isnumeric():
            print('Insira uma Data Valida.')
            continue
        if data.count('/') == 2 and data != '//':
            dia, mes, ano = data.split('/')
            if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and 1900 <= int(ano) <= 2024:
                return data.strip(' ')
            else:
                print ('Dia/Mes/Ano Invalido(s).')
        else:
            print('A data deve seguir o padrao dd/mm/aaaa')

def Login():
    while True:
        login = input('Login: ')
        if login == '':
            print('Error! Entrada Vazia.')
            continue
        return login.strip(' ')
    
def tele():
    while True:
        tele = input('Telefone (Apenas Numeros): ')
        if tele == '':
            print('Error! Entrada Vazia.')
            continue
        elif not tele.isnumeric():
            print('Insira apenas numeros.')
            continue
        else:
            if 9 <= len(tele) <= 11:
                return tele
            else:
                print('O numero deve ter entre 9 e 11 caracteres.')

def funcao():
    while True:
        funcao = input('Qual a funcao? (Digite "1" ou "2"): \n1 - Funcionario \n2 - Gerente\n')
        if funcao == '':
            print('Error! Entrada Vazia.')
            continue
        elif not funcao.isnumeric():
            print('Insira apenas numeros.')
            continue
        return funcao.strip(' ')
