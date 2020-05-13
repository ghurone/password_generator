from secrets import choice
from os import system, name

import pyperclip


def clear():
    return system('cls' if name == 'nt' else 'clear')


def password(tam=12, c_esp=True, c_upp=True, c_num=True):
    pass_list = 'abcdefghijklmnopqrstuvwxyz'
    upp_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    esp_list = '!@#$%&*'
    num_list = '1234567890'

    pwd = ''

    if c_esp:
        pass_list += esp_list

    if c_upp:
        pass_list += upp_list

    if c_num:
        pass_list += num_list

    for i in range(tam):
        pwd += choice(pass_list)

    return pwd


def title():
    print('''╔═════════════════╗
║ Password Master ║
╚═════════════════╝''')
    print('Created by: Ghusoft')


while True:
    title()

    tam = int(input('Tamanho da senha: '))
    c_esp = input('Caracteres especiais (!@#$%&*)?(y,n) ')
    c_upp = input('Caracteres maiúsculos?(y,n) ')
    c_num = input('Caracteres numéricos?(y,n) ')

    if c_esp.lower() == 'y':
        c_esp = True
    else:
        c_esp = False

    if c_upp.lower() == 'y':
        c_upp = True
    else:
        c_upp = False

    if c_num.lower() == 'y':
        c_num = True
    else:
        c_num = False

    senha = password(tam, c_esp, c_upp, c_num)
    pyperclip.copy(senha)

    print(f'Sua senha é: {senha}')
    print('Senha copiada para o clipboard!')
    esc = input('Deseja gerar outra senha?(y,n) ')

    if esc.lower() == 'n':
        break
    else:
        clear()
        continue
