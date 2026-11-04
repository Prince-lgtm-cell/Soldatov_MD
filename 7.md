#1
a=[1,3,0,4,3,1,0,2,0,0,3,1]
b=[]
for i in a:
    if int(i) == 0:
        b.append(sum(a)/len(a))
    else:
        b.append(int(i))
print(b)

#2
a = [4,-2,12,34,6,-76,98,1,-5,-7565,68,-67,67676767]
b=[ ]
c=[ ]
for i in a:
    if i>0:
        b.append(i)
    if i<0:
        c.append(i)
print(b)
print(c)

#3

a = [2,4,6,8,10,20,40,50]
b=[ ]
for i in a:
    if i>=15:
        b.append(i)
    if i<15:
        b.append(i*2)
print(a)
print(b)

#4

a = [2,4,6,8,10,20,40,50,111,32,423,77,12,91,31,1,10,24,17,4]
b=[]
for i in a:
    if i%2!=0:
        b.append(int(i))
x=sorted(b)
x.reverse()
print(a)
print(x)

#5

a = [2,4,6,8,10,20,40,2,111,4]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(a)
print(b)

#6
a = []
s=0
for i in range(10):
    x=int(input())
    a.append(x)
for i in a:
    if i > 5:
        s+=i
print(s)

#7
a = [5,123,9,540,75,34,21]
print(a)
b=[]
mi=99999
ma=1
for x in a:
    if x<mi:
        mi=x
    if x>ma:
        ma=x

for i in a:
    if i == ma:
        b.append(mi)
    if i == mi:
        b.append(ma)
    if i!=ma and i!=mi:
        b.append(i)
print(b)

#8
a=[1,3,0,4,3,1,0,2,0,0,3,1]
b=[]
for i in a:
    if int(i) == 0:
        b.append(sum(a)/len(a))
    else:
        b.append(int(i))
print(b)

#9
a=[1,3,0,4,3,1,0,2,1,7]
b=[2,7,1,3,6,8,1,2,4,8]
c=[]
print(a)
print(b)
for i in a:
    c.append(i)
a.clear()
for i in b:
    a.append(i)
b.clear()
for i in c:
    b.append(i)
print('')
print(a)
print(b)

#10
a=[1,33,0,4,3,1,20,2,1,7,1,15,19,1,3]
b=[]
for i in a:
    if i > 20:
        b.append(1)
    elif i < 10:
        b.append(0)
    else:
        b.append(i)
print(a,b)

#11
a=[1,33,0,4,3,1,20,2,1,7,1,15,19,1,3]
b=[]
for i in a:
    if i%2==0 and i<10:
        b.append(i)
b.sort()
if len(b)==0:
    print('Нету таких')
else:
    print(b)

#12
a=[1,3,0,4,3,1,0,2,1,7]
b=[2,7,1,3,6,8,1,2,4,8]
c=[]
print(a)
print(b)
for i in a:
    c.append(i)
a.clear()
for i in b:
    a.append(i)
b.clear()
for i in c:
    b.append(i)
print('')
print(a)
print(b)

#13
a = [2,4,6,8,10,20,40,50]
b=[ ]
for i in a:
    if i>=15:
        b.append(i)
    if i<15:
        b.append(i*2)
print(a)
print(b)

#14
a=[]
b=[]
for i in range(10):
    x = int(input())
    a.append(x)
s=(sum(a)/len(a))
for i in a:
    if i > s:
        b.append(1)
    else:
        b.append(i)
print(b)

#15
a = [2,4,6,8,10,20,40,50,111,32,423,77,12,91,31,1,10,24,17,4]
b=[]
for i in a:
    if i%2!=0:
        b.append(int(i))
x=sorted(b)
x.reverse()
print(a)
print(x)
