import os

def cls():
    os.system('cls' if os.name == 'nt' and os.name == 'posix' else 'clear')

def disable(time):
    os.system('shutdown /s /t ' + time)


def reload(time):
    os.system('shutdown/r /t ' + time)


def cancelShutdown():
    os.system('shutdown -a')

while True:
    cls()
    number = input("1. Вимкнення комп'ютера\n2. Перезавантаження комп'ютера\nВаш вибір:")
    s = int(input('Введіть кількість секунд: '))
    m = int(input('Введіть кількість хвилин: '))
    h = int(input('Введіть кількість годин: '))

    genTime = s + m * 60 + h * 3600
    if number == '1':
        disable(str(genTime))
    elif number == '2':
        reload(str(genTime))

    print("Для відміни натисніть '3'")
    if input() == '3':
        cancelShutdown()