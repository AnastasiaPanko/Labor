from random import randint
import random
import string
import datetime


def generateElement(type):
  if type == 1:
    return randint(0, 100)


  if type == 2:
    return random.random()

  if type == 3:
    return random.choice(string.ascii_letters)

  if type == 4:
    generatedType = randint(1, 3)
    return generateElement(generatedType)


print("Введіть кількість елементів в масиві:\n10\n100\n1000\n10000\n100000\n1000000\n10000000")
numberElements = int(input())
print("Введіть номер типу елементів:\n1.int\n2.float\n3.char\n4.mixed")
typeElements = int(input())

i = 0
elements = []

start = datetime.datetime.now()
while i < numberElements:
  generateElement(typeElements)
  i += 1
  if i == numberElements:
    break
finish = datetime.datetime.now()
timer = finish - start
print("Время выполнения: ", timer)
file = open("result.txt", "w+")

file.write("Кількість елементів: ")
file.write(str(numberElements))
file.write("\nТип елементів: ")
file.write(str(typeElements))
file.write("\nЧас заповнення: ")
file.write(str(timer))
act = file.read()
print(act)
file.close()
