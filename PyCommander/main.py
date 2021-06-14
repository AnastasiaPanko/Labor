import os

print("1. Переглянути список директорій і файлів в поточній папці")
print("2. Показ поточної директорії")
print("3. Створення папки")
print("4. Зміна директорії")
print("5. Створення текстового файлу")
print("6. Перейменування файла")
print("7. Видалення файлів")
print("8. Видалення каталогу")
print("9. Завершить програму")

while True:
    number = int(input("Введіть номер операції:"))

    if (number == 1):
        print("Список папок та файлів:", os.listdir())

    elif (number == 2):
        print("Поточна директорія:", os.getcwd())

    elif (number == 3):
        print("Створення директорії")
        name = str(input("Введіть назву директорії:"))

        if not os.path.isdir(name):
            os.mkdir(name)
        print("Відображення змін в директорії", os.listdir())

    elif (number == 4):
        print("Зміна директорії на ")
        name = str(input("Введіть назву директорії:"))
        os.chdir(name)
        print("Відображення змін в директорії", os.listdir())

    elif (number == 5):
        print("Створення текстового файлу '.text'")
        namefile = str(input("Введіть назву файла з *.txt:"))
        text_file = open(name, "w")
        text_file.write("Це текстовий файл")
        print("Відображення змін в директорії", os.listdir())

    elif (number == 6):
        namefile = str(input("Введіть назву файла, який треба переіменувати з *.txt:"))
        namefile2 = str(input("Введіть назву файла, на яку назву треба перейменувати з *.txt:"))
        print("Перейменування файла на 'renamed'", os.rename(namefile, namefile2))
        print("Відображення змін в директорії", os.listdir())

    elif (number == 7):
        namefile = str(input("Введіть назву файла з *.txt:"))
        print("Видалення файлу", os.remove(namefile))
        print("Відображення змін в директорії", os.listdir())

    elif (number == 8):
        name = str(input("Введіть назву директорії:"))
        print("Видалення каталогу 'name'", os.rmdir(name))
        print("Відображення змін в директорії", os.listdir())

    elif (number == 9):
        break