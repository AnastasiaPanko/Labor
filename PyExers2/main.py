import math
a = input("")
a = int(a)
print("Задача 41")
f = 1
d = 5
k = 3
if f >= 1 and f <= 3:
    print("f входить в інтервал (1;3)")
    print("f =", f)
if d >= 1 and d <= 3:
    print("d входить в інтервал (1;3)")
    print("d =", d)
if k >= 1 and k <= 3:
    print("k входить в інтервал (1;3)")
    print("k =", k)
print("************************************************")
print("Задача 51")
a = (input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a == 0:
    print("a не може дорівнювати 0. Введіть інші дані")
    import sys
    sys.exit(0)
print("Перетворюємо біквадратне рівняння в квадратне")
dis = b * b - 4 * a * c
if dis <= 0:
    print("Дискримінант є від'ємний")
    import sys
    sys.exit(0)
print("Дискримінант: ", dis)
t1 = (-b + math.sqrt(dis)) / 2 * a
t2 = (-b - math.sqrt(dis)) / 2 * a
print("Корені квадратного рівняння")
print("t1 = ", t1)
print("t2 = ", t2)
print("Повертаємося в біквадратне рівняння")
if t1 > 0:
    x1 = math.sqrt(t1)
    print("x1 = ", x1)
elif t1 < 0:
    print("Від'ємне значення не можна добути з під кореня")
if t2 > 0:
    x2 = math.sqrt(t2)
    print("x2 = ", x2)
elif t2 < 0:
    print("Від'ємне значення не можна добути з під кореня")
print("************************************************")
print("Задача 33")
print("Пункт а")
x = int(input("x = "))
y = int(input("y = "))
if x > y:
    print("max = x = ", x)
elif y > x:
    print("max = y = ", y)
print("Пункт б")
if x < y:
    print("min = x = ", x)
else:
    print("min = y = ", y)
print("Пункт в")
if x > y:
    print("max = x = ", x)
    print("min = y = ", y)
elif y > x:
    print("max = y = ", y)
    print("min = x = ", x)
print("************************************************")
print("Задача 43")
const1 = int(input("const1 = "))
const2 = int(input("const2 = "))
const3 = int(input("const3 = "))
if const1 > 0:
    print("const1 = ", pow(const1, 2))
elif const1 < 0:
    print("Поміняйте значення змінної")
if const2 > 0:
    print("const2 = ", pow(const2, 2))
elif const2 < 0:
    print("Поміняйте значення змінної")
if const3 > 0:
    print("const3 = ", pow(const3, 2))
elif const3 < 0:
    print("Поміняйте значення змінної")
print("************************************************")
print("Задача 53")
#a = int(input("a = "))
a= input("")
a = int(a)
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))
e = int(input("e = "))
f = int(input("f = "))
g = int(input("g = "))
h = int(input("h = "))

f=(x-e)*(h-f)-(y-f)*(g-e)

f1 = (a-e)*(h-f)-(b-f)*(g-e)

f2=(c-e)*(h-f)-(d-f)*(g-e)

if ((f1>0) and (f2>0)) or ((f1<0) and (f2<0)):
    print("Належать")
else:
    print("Не належать")
print("************************************************")
print("Задача 34")
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
if (x >= y) and (x >= z):
    max = x
elif (y >= x) and (y >= z):
    max = y
elif (z >= y) and (z >= x):
    max = z
print("max = ", max)
if (x <= y) and (x <= z):
    min = x
elif (y <= x) and (y <= z):
    min = y
elif (z <= y) and (z <= x):
    min = z
print("min = ", min)
print("************************************************")
print("Задача 44")
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
if (x + y + z <100):
    if((x < y) and (x < z)):
        x = (y+z)/2
    elif (y < z):
        y = (x+z)/2
    else:
        z = (x+y)/2
else:    
    if(x<y):
       x = (y+z)/2
    else:
       y = (x+z)/2
print("************************************************")
print("Задача 54")
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
x3 = int(input("x3 = "))
y3 = int(input("y3 = "))
if (x1 == x2) and (y1 == y2) or (x1 == x3) and (y1 == y3) or (x2 == x3) and (y2 == y3):
    print("Неможливо виконати")
if((x1<=0 and x2>=0) or (x1>=0 and x2<=0) or (x3<=0 and x2>=0) or (x3>=0 and x2<=0) or (x3<=0 and x1>=0) or (x3>=0 and x1<=0)):
    if((y1<=0 and y2>=0) or (y1>=0 and y2<=0) or (y3<=0 and y2>=0) or (y3>=0 and y2<=0) or (y3<=0 and y1>=0) or (y3>=0 and y1<=0)):
        print("Координати входять")
    else:
        print("y є не коректним")
else:
    print("x є не коректним")
print("************************************************")
print("Задача 35")
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
print("Пункт а")
if (x + y + z > x * y * z):
    print("max x + y + z: ", x + y + z)
else:
    print("max x * y * z: ", x * y * z)
print("Пункт б")
if (x + y + z / 2 > x * y * z):
    min = x * y * z
else:
    min = x + y + z / 2
print("min: ", pow(min, 2) + 1)
print("************************************************")
print("Задача 55")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if ((a < c) and (b < d)) or ((a < d) and (b < c)):
    print("Можна вмістити в прямокутник")
else:
    print("Не можна")
print("************************************************")
print("Параграф 3")

print("Задача 61")
x = float(input("x = "))
print("Число Х", x, "Ціле число: ", int(x), "Заокуглення: ", round(x))
print("************************************************")
print("Задача 62")
a = int(input("a = "))
if a % 2 == 0:
    print("Число парне")
else:
    print("Число не парне")
print("************************************************")
print("Задача 63")
a = int(input("Відємне число: "))
b = int(input("Додатнє число: "))
r = int(input("r = "))
s = int(input("s = "))

if (a % b) == r or (a % b) == s:
    print("Остача рівна r або s")
else:
    print("Остача не рівна")
print("************************************************")
print("Задача 73")
k = int(input("k = "))
n = int(input("n = "))
if k > n:
    n = k
elif n > k:
    k = n
elif n == k:
    n = 0
    k = 0
print("k = ", k)
print("n = ", n)
print("Задача 74")
print("************************************************")
n = int(input("Введите возраст до 100 лет"))
while n <= 100:
    if (n % 10) == 1:
        print(n, "рік")
    elif ((n % 10) == 2) or ((n % 10) == 3) or ((n % 10) == 4):
        print(n, "роки")
    elif ((n % 10) == 5) or ((n % 10) == 6) or ((n % 10) == 7) or ((n % 10) == 8) or ((n % 10) == 9) or ((n % 10) == 0):
        print(n, "років")
print("************************************************")
print("Задача 64")
print("а > 99")
a = int(input("a = "))
print("Кількість сотень:", a // 100)
print("************************************************")