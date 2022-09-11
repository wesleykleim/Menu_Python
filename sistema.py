

from unittest import suite
from imports.menu import *
from time import sleep





cabecalho( 'SITEMA CHALENGE PYTHON v1.0')
cadastro = []
cadastroEmpresa = []
vagas = ['Empresa: IBM','Cargo: Estagiario','Salario: R$3000,00']
while True:
    resposta = menu(['Cadastrar Empresa', 'Cadastrar Candiadato', 'Ver Candidato Cadastrado','Ver Vagas', 'Sair do Sistema'])

    if resposta == 1:

       cabecalho('Cadastrar Empresa')
       print('Informe os dados da empresa: ')
       empresa = input('Digite o nome da empresa: ')
       ramo = input('Qual o ramo de atividade: ')
       cnpj = input(('Digite o número do CNPJ: '))

       cadastroEmpresa.append(f'Nome empresa: {empresa}')
       cadastroEmpresa.append(f'Ramo de Atividade: {ramo}')
       cadastroEmpresa.append(f'CNPJ: {cnpj}')

       for i in (range(len(cadastroEmpresa))):
        print(cadastroEmpresa[i])


    elif resposta == 2:

        cabecalho('Cadastrar Candiadato')
    
        print('Informe seus dados!')
        usuario = input('informe seu Nome: ')
        cpf = input('Digite o seu cpf:')
        dtNasc = (input('Dite a data de nascimento: '))
        genero = input('Digite sexo: ')
        apelido = input('Digite seu apelido: ')  

        cadastro.append(f'Nome: {usuario}')
        cadastro.append(f'CPF: {cpf}')
        cadastro.append(f'Data de Nascimento: {dtNasc}')
        cadastro.append(f'Genero: {genero}')
        cadastro.append(f'Apelido: {apelido}')
        print("Cadastrado com seucesso!")

    elif resposta == 3:
        cabecalho('Ver Candidato Cadastrado')
        if len(cadastro) > 1:

            for i in range(len(cadastro)):
             print(cadastro[i])
        else:
            print('Nenhum cadidato encontrado') 
           


    elif resposta == 4:
        cabecalho('Ver Vagas')
        for i in range(len(vagas)):
             print(vagas[i])

    elif resposta == 5:
        print('\033[32mSaindo do sistema... Até logo!\033[m')
        break
    else:
        cabecalho('\033[31mERRO! Digite um número com uma opção válida!\033[m')
    sleep(2)