from msvcrt import getch
from bot import *
import getpass
timer = 15

def menu(path):
    clear()
    show_menu()
    print(f"Olá {getpass.getuser().title()}, Bem vindo(a)")
    key = getch().decode()
    while key != '3':
        clear()
        show_menu()
        if key == '1':
            run(timer)
        elif key == '2':
            menu_config(timer)
        else:
            print('Opção invalida!')
            sleep(1)
        clear()
        show_menu()
        key = getch().decode()

def menu_config(timer):
    clear()
    show_menu_config()
    key = getch().decode()
    while key != '2':
        clear()
        show_menu_config()
        if key == '1':
            clear()
            changeTimer()
            break
        else:
            print('Opção invalida!')
            sleep(1)
        clear()
        show_menu_config()
        key = getch().decode()

def changeTimer():
    global timer
    print(f"Tempo atual de espera no mapa [{timer} {'Minuto' if timer == 1 else 'Minutos'}]")
    timer = validadeTimer(input('Digite quanto tempo deseja(em minutos):\n'))

def validadeTimer(parameter):
    while not parameter.isdigit():
        clear()
        parameter = input('Somente numeros, digite novamente o tempo corretamente:\n')
    return parameter

def show_menu():
    print(
        f'+--------------------------------------------------------------+\n'
        f'│                 --=[+ BombCryptoBOT +]=--                    │\n'
        f'│       [1] Iniciar BOT // [2] Configuração // [3] Sair        │\n'
        f'+--------------------------------------------------------------+'
    )

def show_menu_config():
    print(
        f'+--------------------------------------------------------------+\n'
        f'│                 --=[+ Configuração Bot +]=--                 │\n'
        f'│           [1] Ajustar tempo em mapa // [2] Sair              │\n'
        f'+--------------------------------------------------------------+'
    )
