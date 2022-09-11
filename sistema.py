from imports.menu import *
from time import sleep
cabecalho( 'SITEMA CHALENGE PYTHON v1.0')
while True:
    resposta = menu(['Cadastrar Empresa', 'Cadastrar Candiadato', 'Ver Vagas', 'Sair do Sistema'])
    if resposta == 1:
       cabecalho('Cadastrar Empresa')
    elif resposta == 2:
        cabecalho('Cadastrar Candiadato')
    elif resposta == 3:
        cabecalho('Ver Vagas')
    elif resposta == 4:
        print('\033[32mSaindo do sistema... Até logo!\033[m')
        break
    else:
        cabecalho('\033[31mERRO! Digite um número com uma opção válida!\033[m')
    sleep(2)