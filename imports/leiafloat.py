def leiafloat(msg):
    while True:
        try:
            n  = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interronpidade pelo usuário\033[m')
            return 0
        else:
            return n

num2 = leiafloat('Digite um valor: ')
print(f'O valor digitado foi {num2}')