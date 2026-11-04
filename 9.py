#1
n = int(input("Количество строк: "))
m = int(input("Количество столбцов: "))

B = []
for z in range(n):
    r = list(map(int, input().split()))
    B.append(r)

for i in range(n):
    r = B[i]

    ma = r.index(max(r))
    mi = r.index(min(r))

    if ma == mi:
        continue

    r[0], r[ma] = r[ma], r[0]
    mi = r.index(min(r))
    r[-1], r[mi] = r[mi], r[-1]

print("Полученная матрица:")
for r in B:
    print(*r)

#2
n = int(input("Количество строк: "))
m = int(input("Количество столбцов: "))

A = []

for i in range(n):
    r = list(map(int, input().split()))
    A.append(r)

for i in range(n):
    A[i][0], A[i][-1] = A[i][-1], A[i][0]

for r in A:
    print(*r)

#3
n = int(input("Количество строк: "))
m = int(input("Количество столбцов: "))

A = []

for i in range(n):
    r = list(map(float, input().split()))
    A.append(r)

ma = A[0][0]
max_i = 0
max_j = 0

for i in range(n):
    for j in range(m):
        if A[i][j] > ma:
            ma = A[i][j]
            max_i = i
            max_j = j

A[0], A[max_i] = A[max_i], A[0]

for i in range(n):
    A[i][0], A[i][max_j] = A[i][max_j], A[i][0]

for r in A:
    print(*r)

#4
n = int(input("Размер матрицы: "))

A = []

for i in range(n):
    r = list(map(int, input().split()))
    A.append(r)

for i in range(n):
    for j in range(n):
        if A[i][j] < 0:
            A[i][j] = 0
        elif A[i][j] > 0:
            A[i][j] = 1

print("Нижняя треугольная матрица:")

for i in range(n):
    print("  " * (n - i - 1), end="")
    for j in range(i + 1):
        print(A[i][j], end=" ")
    print()

#5
n = int(input("Количество строк: "))
m = int(input("Количество столбцов: "))

A = []

for i in range(n):
    r = list(map(int, input().split()))
    A.append(r)

for i in range(n):
    mi = A[i].index(min(A[i]))

    if A[i][mi] % 2 == 0:
        A[i][mi] = 0
    else:
        A[i][mi] = 1

print("Новая матрица:")
for r in A:
    print(*r)

#6
n = int(input("Размер матрицы (нечётное число): "))

A = []

for i in range(n):
    r = list(map(int, input().split()))
    A.append(r)

ma = A[0][0]
max_i = 0
max_j = 0

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            if A[i][j] > ma:
                ma = A[i][j]
                max_i = i
                max_j = j

c = n // 2

A[c][c], A[max_i][max_j] = A[max_i][max_j], A[c][c]

print("Полученная матрица:")
for r in A:
    print(*r)

#7
n = int(input("Размер матрицы: "))

A = []

for i in range(n):
    r = list(map(int, input().split()))
    A.append(r)

B = []

for i in range(n):
    B.append(A[i][i])

s = sum(B)

print("Диагональные элементы:", B)
print("След матрицы:", s)

if s != 0:
    for i in range(n):
        if (i + 1) % 2 == 0:
            for j in range(n):
                A[i][j] = A[i][j] / s

    print("Полученная матрица:")
    for r in A:
        print(*r)
else:
    print("След матрицы равен нулю, деление невозможно.")

#8
n = int(input("Размер матрицы: "))

A = []

for i in range(n):
    r = list(map(int, input().split()))
    A.append(r)

B = []

for i in range(n):
    r = []
    for j in range(n):
        r.append(A[j][i])
    B.append(r)

print("Транспонированная матрица:")
for r in B:
    print(*r)

#9
n = int(input("Размер матрицы: "))

A = []

for i in range(n):
    r = list(map(int, input().split()))
    A.append(r)

ma = A[0][0]
max_i = 0
max_j = 0

for i in range(n):
    for j in range(n):
        if abs(A[i][j]) > abs(ma):
            ma = A[i][j]
            max_i = i
            max_j = j

B = []

for i in range(n):
    if i != max_i:
        r = []
        for j in range(n):
            if j != max_j:
                r.append(A[i][j])
        B.append(r)

print("Наибольший по модулю элемент:", ma)
print("Новая матрица:")

for r in B:
    print(*r)

#10
m = int(input("Количество строк: "))
n = int(input("Количество столбцов: "))

A = []

for i in range(m):
    f = list(map(int, input().split()))
    A.append(f)

k = int(input("Введите номер строки k: "))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if A[k - 1][j] > A[k - 1][j + 1]:
            for r in range(m):
                A[r][j], A[r][j + 1] = A[r][j + 1], A[r][j]

print("Полученная матрица:")
for f in A:
    print(*f)

#11
m = int(input("Количество строк: "))
n = int(input("Количество столбцов: "))

A = []

for i in range(m):
    r = list(map(int, input().split()))
    A.append(r)

min_p = None
min_c = -1

for j in range(n):
    p = 1
    v = True

    for i in range(m):
        if abs(A[i][j]) > 10:
            v = False
            break
        p *= A[i][j]

    if v:
        if min_p is None or p < min_p:
            min_p = p
            min_c = j

if min_c != -1 and n > 1:
    if min_c < n - 1:
        o = min_c + 1
    else:
        o = min_c - 1

    for i in range(m):
        A[i][min_c], A[i][o] = A[i][o], A[i][min_c]

    print("Полученная матрица:")
    for r in A:
        print(*r)
else:
    print("Подходящий столбец для перестановки не найден.")

#12
n = int(input("Количество строк: "))
m = int(input("Количество столбцов: "))

A = []

for i in range(n):
    r = list(map(int, input().split()))
    A.append(r)

for i in range(n - 1):
    for j in range(m):
        A[i][j] -= A[n - 1][j]

print("Полученная матрица:")
for r in A:
    print(*r)

#13
n = int(input("Количество строк: "))
m = int(input("Количество столбцов: "))

A = []

for i in range(n):
    r = list(map(int, input().split()))
    A.append(r)

ma = A[0][0]
mi = A[0][0]

max_i = 0
max_j = 0
min_i = 0
min_j = 0

for i in range(n):
    for j in range(m):
        if A[i][j] > ma:
            ma = A[i][j]
            max_i = i
            max_j = j

        if A[i][j] < mi:
            mi = A[i][j]
            min_i = i
            min_j = j

A[max_i][max_j], A[min_i][min_j] = A[min_i][min_j], A[max_i][max_j]

print("Полученная матрица:")
for r in A:
    print(*r)

#14
n = int(input("Размер матрицы: "))

A = [[0] * n for i in range(n)]

t = 0
b = n - 1
left = 0
right = n - 1

num = 1

while t <= b and left <= right:

    for j in range(left, right + 1):
        A[t][j] = num
        num += 1
    t += 1

    for i in range(t, b + 1):
        A[i][right] = num
        num += 1
    right -= 1

    if top <= b:
        for j in range(right, left - 1, -1):
            A[b][j] = num
            num += 1
        b -= 1

    if left <= right:
        for i in range(b, top - 1, -1):
            A[i][left] = num
            num += 1
        left += 1

print("Полученная матрица:")
for r in A:
    print(*r)

#15
n = int(input("Количество строк: "))
m = int(input("Количество столбцов: "))

A = []

for i in range(n):
    r = list(map(int, input().split()))
    A.append(r)

max_sum = -1
max_r = -1

for i in range(n):
    d = True
    s = 0

    for j in range(m):
        if A[i][j] % 2 == 0:
            d = False
            break
        s += abs(A[i][j])

    if d and s > max_sum:
        max_sum = s
        max_r = i

if max_r != -1:
    print("Номер строки:", max_r + 1)
    print("Строка:", *A[max_r])
    print("Максимальная сумма модулей:", max_sum)
else:
    print("Строк с одними нечётными элементами нет.")
