#python3


def traco():
    print("--------------------------------------------------------------------------------------")


def rep10():
    x = 0
    mac = input("insira o mac  =")
    while x < 10:
        print(f'{mac}')
        x = x + 1


def rep20():
    x = 0
    mac = input("insira o mac  =")
    while x < 20:
        print(f'{mac}')
        x = x + 1


def rep30():
    x = 0
    mac = input("insira o mac  =")
    while x < 30:
        print(f'{mac}')
        x = x + 1


def rep40():
    x = 0
    mac = input("insira o mac  =")
    while x < 40:
        print(f'{mac}')
        x = x + 1


def rep50():
    x = 0
    mac = input("insira o mac  =")
    while x < 50:
        print(f'{mac}')
        x = x + 1


# inicio do código

traco()

print("===================================================== __REPETIDOR DE MAC__V.02======================================================================")

traco()

print("[10]")
print("[20]")
print("[30]")
print("[40]")
print("[50]")

mac = int(input("quantas vezes você quer que repita o mac?"))

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
