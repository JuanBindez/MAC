#python3
import os


class Color():
    VERDE = '\033[92m'
    VERMELHO = '\033[91m'
    AMARELO = '\033[93m'
    AZUL = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    VERDE_CLARO = '\033[1;92m'
    NEGRITO = '\033[;1m'
    RESET = '\033[0m'


def traco():
    print(Color.AMARELO + "--------------------------------------------------------------------------------------" + Color.RESET)


def rep10():
    x = 0
    mac = input(Color.AZUL + "insira o mac  =")
    while x < 10:
        print(f'{mac}')
        x = x + 1


def rep20():
    x = 0
    mac = input(Color.AZUL + "insira o mac  =")
    while x < 20:
        print(f'{mac}')
        x = x + 1


def rep30():
    x = 0
    mac = input(Color.AZUL + "insira o mac  =")
    while x < 30:
        print(f'{mac}')
        x = x + 1


def rep40():
    x = 0
    mac = input(Color.AZUL + "insira o mac  =")
    while x < 40:
        print(f'{mac}')
        x = x + 1


def rep50():
    x = 0
    mac = input(Color.AZUL + "insira o mac  =")
    while x < 50:
        print(f'{mac}')
        x = x + 1


print(Color.AMARELO +"===================================================== __REPETIDOR DE MAC__V.02======================================================================" + Color.RESET)


print("[10]")
print("[20]")
print("[30]")
print("[40]")
print("[50]")

try:
    mac = int(input(Color.VERDE + "quantas vezes você quer que repita o mac?"))
except ValueError:
    os.system("clear")
    print(Color.VERMELHO + "digite apenas numeros!")
    

x = 0

if mac == 10:
    rep10()

if mac == 20:
    rep20()

if mac == 30:
    rep30()

if mac == 40:
    rep40()

if mac == 50:
    rep50()
