#1
a = int(input("Введи значение для переменной a: "))
b = int(input("Введи значение для переменной b: "))
c = int(input("Введи значение для переменной c: "))

print(a + b + c)

#2
a = int(input("Введи значение для переменной a: "))
b = int(input("Введи значение для переменной b: "))

area = 0.5 * a * b

print(area)

#3
n = int(input("Введи значение для переменной n: "))

n = n % 1440
hours = n // 60
minutes = n % 60

print(hours, minutes)

#4
def calculate_lace_length():
    a = int(input("Введи значение для переменной a: "))
    b = int(input("Введи значение для переменной b: "))
    l = int(input("Введи значение для переменной l: "))
    n = int(input("Введи значение для переменной n: "))

    total_length = 2 * l + (2 * n - 1) * a + 2 * (n - 1) * b
    print(total_length)

calculate_lace_length()

#5
def find_minimum():
    a = int(input("Введи значение для переменной a: "))
    b = int(input("Введи значение для переменной b: "))
    c = int(input("Введи значение для переменной c: "))

    print(min(a, b, c))

find_minimum()

#6
def check_chess_colors():
    col1 = int(input("Введи значение для переменной col1: "))
    row1 = int(input("Введи значение для переменной row1: "))
    col2 = int(input("Введи значение для переменной col2: "))
    row2 = int(input("Введи значение для переменной row2: "))

    if (col1 + row1) % 2 == (col2 + row2) % 2:
        print("Да")
    else:
        print("Нет")

check_chess_colors()

#7
def is_leap_year():
    year = int(input("Введи значение для переменной year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Да")
    else:
        print("Нет")

is_leap_year()

#8
def count_matching_numbers():
    a = int(input("Введи значение для переменной a: "))
    b = int(input("Введи значение для переменной b: "))
    c = int(input("Введи значение для переменной c: "))

    if a == b == c:
        print(3)
    elif a == b or b == c or a == c:
        print(2)
    else:
        print(0)

count_matching_numbers()

#9
def check_chocolate_break():
    n = int(input("Введи значение для переменной n: "))
    m = int(input("Введи значение для переменной m "))
    k = int(input("Введи значение для переменной k: "))

    if k < n * m and (k % n == 0 or k % m == 0):
        print("Да")
    else:
        print("Нет")

check_chocolate_break()