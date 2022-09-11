
from datetime import date
from unittest import suite
from imports.menu import *
from time import sleep







cabecalho( 'SITEMA CHALENGE PYTHON v1.0')
while True:
    resposta = menu(['Cadastrar Empresa', 'Cadastrar Candiadato', 'Ver Candidato Cadastrado','Ver Vagas', 'Sair do Sistema'])
    if resposta == 1:
       cabecalho('Cadastrar Empresa')
    elif resposta == 2:
        cabecalho('Cadastrar Candiadato')

        cadastro = []
        print('Informe seus dados!')
        usuario = input('informe seu Nome: ')
        cpf = int(input('Digite o seu cpf: '))
        dtNasc = (input('Dite a data de nascimento: '))
        genero = input('Digite sexo: ')
        apelido = input('Digite seu apelido: ')  

        cadastro.append(f'Nome: {usuario}')
        cadastro.append(f'CPF: {cpf}')
        cadastro.append(f'Data de Nascimento: {dtNasc}')
        cadastro.append(f'Genero: {genero}')
        cadastro.append(f'Apelido: {apelido}')

    elif resposta == 3:
        cabecalho('Ver Candidato Cadastrado')
        for i in(range(len(cadastro))):
            print(cadastro[i])


    elif resposta == 4:
        cabecalho('Ver Vagas')
    elif resposta == 5:
        print('\033[32mSaindo do sistema... Até logo!\033[m')
        break
    else:
        cabecalho('\033[31mERRO! Digite um número com uma opção válida!\033[m')
    sleep(2)