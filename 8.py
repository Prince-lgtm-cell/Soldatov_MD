#1
def f(x):
    return sum(x),(sum(x)/len(x))

a=[1,2,3,4,5,6,7,8,9]
b=[1,2,3,4,5,6,7,8]
c=[1,2,3,4,5,6,7,8]
print(f(a))
print(f(b))
print(f(c))

#2
def f(x,y):
    return x*y

a,b=int(input()),int(input())
print(f(a,b))

c,d=int(input()),int(input())
print(f(c,d))

e,g=int(input()),int(input())
print(f(e,g))

#3
def f(s):
    w = s.split()
    r = []
    for x in w:
        c = sorted(x)
        y = ''.join(c)
        r.append(y)
    return ' '.join(r)

s = input()
r = f(s)
print(r)

#4
from math import*
def g(c,r,t):
    if dist(c,t)<r:
        return 1
    else:
        return 0
k=0
print('Центр:')
c = [int(input())*2,int(input())*2]
print('Радиус:')
r=int(input())
print('Т1:')
p = [int(input()),int(input())]
print('Т2:')
l = [int(input()),int(input())]
print('Т3:')
f = [int(input()),int(input())]
if g(c,r,p):
    k+=1
if g(c,r,f):
    k+=1
if g(c,r,l):
    k+=1
print(k)

#5
def f(x):
    for i in range(1,x+1):
        if x % i == 0:
            print(i)
x=int(input())
print(f(x))

#6
import math

def f(a, b, c, d, diag):
    p1 = (a + b + diag) / 2.0
    p2 = (c + d + diag) / 2.0
    s1 = math.sqrt(p1 * (p1 - a) * (p1 - b) * (p1 - diag))
    s2 = math.sqrt(p2 * (p2 - c) * (p2 - d) * (p2 - diag))
    return s1 + s2

a = float(input())
b = float(input())
c = float(input())
d = float(input())
diag = float(input())

print(f(a, b, c, d, diag))

#7
def f(n):
    if n == 0:
        return "0000000000"
    s = ""
    while n > 0:
        s = str(n % 8) + s
        n //= 8
    return s.zfill(10)

x = int(input().strip())
print(f(x))

#8
def f(x):
    c=[]
    a=x[0]
    b=x[-1]
    for i in range(0,len(x)):
        if i == 0:
            c.append(b)
        elif i == len(x)-1:
            c.append(a)
        else:
            c.append(x[i])
    return c

A = []
dl=int(input())
for i in range(dl):\
    A.append(int(input()))
print(A)
print(f(A))

#9
def f(x):
    s=1
    c=0
    for i in x:
        s = s * i
    c = sum(x)/len(x)
    return s,c

x = [1,2,3,4,5]
print(f(x))

#10
def f(x):
    a=[]
    x = x.split(' ')
    for i in x:
        a.append(i)
    a.reverse()
    return a

x = input()
print(" ".join(f(x)))

#11
def f(x):
    m=0
    for i in x:
        for n in i:
            if n>m:
                m=n
    return m
x = [[8,8,3],[8,5,6],[1,1,9]]
y = [[4,2,8],[3,7,1],[5,3,6]]
a=[]
a1=[]
b=[]
b1=[]
print(f(x))
print(f(y))
for i in x:
    if f(x) not in i:
        a.append(i)
    else:
        for j in i:
            if j != f(x):
                a1.append(j)
            else:
                a1.append(f(y))
        a.append(a1)
for i in y:
    if f(y) not in i:
        b.append(i)
    else:
        for j in i:
            if j != f(y):
                b1.append(j)
            else:
                b1.append(f(x))
        b.append(b1)
print(x)
print(y)
print(a)
print(b)

#12
def f(x, y, z):
    return (2 * y**2 + 2 * z**2 - x**2)**0.5 / 2

a, b, c = map(float, input().split())

ma = f(a, b, c)
mb = f(b, a, c)
mc = f(c, a, b)

m_ma = f(ma, mb, mc)
m_mb = f(mb, ma, mc)
m_mc = f(mc, ma, mb)

print(round(m_ma, 2), round(m_mb, 2), round(m_mc, 2))

#13
import math
def f(x, y):
    return math.atan2(y, x)

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())

a = f(x1, y1)
b = f(x2, y2)
c = f(x3, y3)

if a <= b and a <= c:
    print(x1, y1)
elif b <= a and b <= c:
    print(x2, y2)
else:
    print(x3, y3)

#14
from math import*
def f(x,y):
    s = dist(x,y)
    return s

print('1 точка')
t1=[int(input()),int(input())]
print('2 точка')
t2=[int(input()),int(input())]
print('3 точка')
t3=[int(input()),int(input())]
print('4 точка')
t4=[int(input()),int(input())]


r1 = f(t1,t2)
r2 = f(t3,t4)
r3 = f(t1,t3)
r4 = f(t1,t4)
a = [r1,r2,r3,r4]
print(max(a))

#15
from math import*
def f(x,y):
    s = dist(x,y)
    return s

print('1 точка')
t1=[int(input()),int(input()),int(input())]
print('2 точка')
t2=[int(input()),int(input()),int(input())]
print('3 точка')
t3=[int(input()),int(input()),int(input())]
print('4 точка')
t4=[int(input()),int(input()),int(input())]


r1 = f(t1,t2)
r2 = f(t3,t4)
r3 = f(t1,t3)
r4 = f(t1,t4)
a = [r1,r2,r3,r4]
print(min(a))
