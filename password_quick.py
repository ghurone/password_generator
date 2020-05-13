from secrets import choice
from os import system, name

import pyperclip  # precisei importar, no futuro crio minha propria função!


def password(tam=12):
    pass_list = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + '1234567890' + '!@#$%&*'
    psd = ''

    for i in range(tam):
        psd += choice(pass_list)

    return psd


def clear():
    return system('cls' if name == 'nt' else 'clear')


while True:
    cp = password()

    print(f'Senha gerada: {cp}')
    print(f'Senha copiada para o clipboard!')
    pyperclip.copy(cp)

    esc = input('Deseja gerar outra senha?(y/n) ')

    if esc.lower() == 'n':
        break
    else:
        clear()
        continue
