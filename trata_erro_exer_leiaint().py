'''
Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\33[31mERRO: Por favor digite um numero inteiro válido\33[m')
            continue # continue joga para o laço novamente.
        except (KeyboardInterrupt):
            print('\n\033[mEntrada de dados interrompida pelo Usuário\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\33[31mERRO: Por favor digite um numero realválido\33[m')
            continue # continue joga para o laço novamente.
        except (KeyboardInterrupt):
            print('\n\033[mEntrada de dados interrompida pelo Usuário\033[m')
            return 0
        else:
            return n

n1 = leiaInt('Digite um Numero Inteiro: ')
n2= leiaFloat('Digite um Numero Real: ')
print(f'O Valor inteiro digitado foi{n1} e o real {n2}')    