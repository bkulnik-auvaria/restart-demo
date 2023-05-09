l0=[1]
n=int(input('Insert a positve integer: '))
for x  in range(n):
    l1=[1]
    print(x)
    for y in range(x):
        l1.append(l0[y]+l0[y+1])
    l1.append(1)
    l0=l1

print(l0)