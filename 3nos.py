a = [int(i) for i in input().split()]
x=max(a[0],a[1],a[2],a[3])
c=a.index(x)
if c==0:
    print(x-a[1],x-a[2],x-a[3])
elif c==1:
    print(x-a[0],x-a[2],x-a[3])
elif c==2:
    print(x-a[0],x-a[1],x-a[3])
else:
    print(x-a[0],x-a[1],x-a[2])

