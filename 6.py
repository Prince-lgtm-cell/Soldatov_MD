#1
a = input("Введите строку: ")
w = a.split()
c = 0

for i in range(len(w)):
    if (w[i].lower())[0] == 'е':
        c += 1
print(c)

#2
a = input("Введите строку: ")
c = a.count(':')
a = a.replace(':', '%')
print(a)
print(c)

#3
a = input("Введите строку: ")
c = a.count('.')
a = a.replace('.', '')
print(a)
print(c)

#4
a = input("Введите строку: ")
c = a.lower().count('а')
a = a.replace('а', 'о').replace('А', 'О')
print(a)
print(c)
print(len(a))

#5
a = input("Введите строку: ")
print(a.lower())

#6
a = input("Введите строку: ")
c = a.lower().count('а')
a = a.replace('а', '').replace('А', '')
print(a, c)

#7
a = input("Введите строку: ")
n = len(a) // 2
a = a[0:n]
a = a.lower().replace('п', '*').replace('П', '*')
print(a)

#8
a = input("Введите строку: ")
w = a.split()
cnt = len(w)
print(c)

#9
a = input("Введите строку: ")
y = input("Введите слово: ")
w = a.lower().split()
y = y.lower()
print(w.count(f'{y}'))

#10
print(input("Введите строку: ").title())

#11
a = input("Введите строку: ")
c = 0
d = []

for i in range(len(a)):
    if a[i] == 'н' or a[i] == 'Н':
        c += 1
    else:
        d.append(c)
        c = 0
d.append(c)

print(a.replace('!','.'))
print(max(d))

#12
a = input("Введите строку: ").replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace("'","")\
    .replace('"','').split()
z = []
for i in range(0, len(a)):
    if a[i][-1] == 'я':
        z.append(a[i])
print(z)

#13
a = input("Введите строку: ")
d = []

for i in range(0, len(a)):
    if a[i] == '(':
        for x in range(i + 1, len(a)):
            if a[x] != ')':
                d.append(a[x])
            else:
                break
    else:
        continue
print(d)

#14
a = input("Введите строку: ").replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace("'","")\
    .replace('"','').lower().split()
z1 = []
for i in range(0, len(a)):
    if a[i][-1] == 'я' or a[i][0] == 'а':
        z1.append(a[i])
print(z1)

#15
a = input("Введите строку: ").lower()
c = 0
for i in range(0, len(a)):
    if a[i] == 'т':
        c += 1
print(c)
