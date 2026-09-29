#1
print("Курс Основы программирования начался")

#2
print((16823 * 12302) % 3092)

#3
age = int(input("Введите возраст:"))
name = input("Введите имя:")

if age >= 16:
    print("Поздравляем вы поступили в ВГУИТ")
else:
    print("Сначала нужно окончить школу!")

if age > 0 and age < 75:
    print("Входит в диапазон")
else:
    print("Не входит в диапазон")

if name != "Иван":
    print("Поступающего зовут не Иван")
else:
    print("Поступающего зовут Иван")

if age < 16:
    print("Осталось учиться в школе:", 16 - age, "лет")

#4
seconds = int(input())

d = seconds // 86400
h = (seconds % 86400) // 3600
m = (seconds % 3600) // 60
s = seconds % 60

print(d, "дн.", h, "ч.", m, "мин.", s, "сек.")

#5
n = int(input())
n = int(n)

result = n + n**2 + n**3 + n**4 + n**5

print(result)


#6
x = int(input())
y = int(input())

x, y = y, x

print("x =", x)
print("y =", y)

#7
number = int(input())

if number % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")