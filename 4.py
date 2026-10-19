#1
a = int(input())
b = int(input())
if a < b:
    for i in range(a,b+1):
        print(i)
else:
    print('Первое число толжно быть меньше')

#2
a = int(input())
b = int(input())
if a < b:
    for i in range(a,b+1):
        print(i)
elif b<a:
    for i in range(a,b-1,-1):
        print(i)
else:
    print(a)


#3
a = int(input())
b = int(input())
if a > b:
    for i in range(a,b-1,-1):
        if i%2!=0
            print(i)
else:
    print('Первое число толжно быть больше')

#4
a = int(input())
c=[]
for i in range(a):
    b = int(input())
    c.append(b)
print(sum(c))


#5
a = int(input())
c=[]
for i in range(1,a+1):
    c.append(i**3)
print(sum(c))


#6
a = int(input())
c=1
for i in range(1,a+1):
    c = c*i
print(c)


#7
a = int(input())
c=1
s=[]
for i in range(1,a+1):
    c = c*i
    s.append(c)
print(sum(s))


#8
a = int(input())
k=0
if a<=9 and a>=1:
    for i in range(1,a):
        k+=int(i*'1')
        print(k+int(i * '1')+int(10**i))


#9
a = int(input())
x = 0
y = 1
t = 0
for i in range(a):
    t += x
    x, y = y, x + y
print(t)

#10
n = int(input("Введите количество чисел"))
k = int(input("Введите порядковый номер начала"))
a, b = 0, 1
t = 0
for i in range(1, k + n):
    if i >= k:
        t += a
    a, b = b, a + b
print(t)
