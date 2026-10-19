print('#1')
#1
a= int(input())
for i in range(a+1):
    if i**2 <= a:
        print(i**2)
print('#2')
#2
a= int(input())
if a>=2:
    for i in range(2,a+1):
        if a%i==0:
            print(i)
            break
print('#3')
#3
a = int(input())
k=2
p=0
for i in range(a):
    k=k*2
    p+=1
print(p,k)
print('#4')
#4
x = int(input())
y = int(input())
c = x
d = 1
while c < y:
    c += c * 0.1
    d += 1
print(d)
print('#5')
#5
a=[]
d=1
while d > 0:
    x=int(input())
    a.append(x)
    if x == 0:
        d == 0
        print(len(a)-1)
        break
print('#6')
#6
a=[]
d=1
while d > 0:
    x=int(input())
    a.append(x)
    if x == 0:
        d == 0
        print(sum(a)/(len(a)-1))
        break
print('#7')
#7
a=[]
d=1
k=0
while d > 0:
    x=int(input())
    if len(a)>0:
        if x > a[-1]:
            k+=1
    else:
        a.append(x)
    a.append(x)
    if x == 0:
        d == 0
        print(k)
        break
print('#8')
#8
a=[]
b=[]
d=1
k=0
while d > 0:
    x=int(input())
    if len(a)>0:
        if x == a[-1]:
            k+=1
        else:
            b.append(k+1)
            k = 0
    else:
        a.append(x)
    a.append(x)
    if x == 0:
        d == 0
        print(max(b))
        break
