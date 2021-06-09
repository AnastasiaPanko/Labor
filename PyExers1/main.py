import math
#1
print("Задача 1")
a = 5
b = 3
print("a+b=", a + b)
print("a-b=", a - b)
print("a*b=", a * b)
#2
print("Задача 2")
x = 4
y = 6
print("Виведення розв'язку:", (math.fabs(x)-math.fabs(y))/(1+math.fabs(x*y)))
#3
print("Задача 3")
print("Об'єм куба:", math.pow(a, 3))
print("Площа куба:", math.pow(a, 2))
#4
print("Задача 4")
print("Середнє арифметичне:", (a + b) / 2)
print("Середнє геометричне:", math.sqrt(a * b))
#5
print("Задача 5")
print("Середнє арифметичне:", math.fabs((a + b)/ 2))
print("Середнє геометричне:", math.sqrt(math.fabs(a * b)))
#6
print("Задача 6")
print("3 сторона:", math.sqrt(a * a + b * b))
print("Площа трикутника:", (a * b) / 2)
#7
print("Задача 7")
t1 = 5
t2 = 6
v1 = 3
v2 = 8
print("Температура суміші:", (t1 + t2) / 2)
print("Об'єм суміші", (v1 + v2) / 2)
#8
print("Задача 8")
n = 5
r = 5
print("Периметр фігури:", 2 * n * r * math.tan(math.pi / n))
#9
print("Задача 9")
r1 = 3
r2 = 8
r3 = 9
print("Опір:", (r1 * r2 * r3) / ((r1 * r2) + (r2 * r3) + (r3 * r1)))
#10
print("Задача 10")
g = 10
h = 8
print("Час падіння:", math.sqrt((2 * g) / h))
