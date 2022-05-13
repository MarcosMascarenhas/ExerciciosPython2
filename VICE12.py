x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)
if x < y < z:
    print(y)
elif x < z < y:
    print(z)
elif y < x < z:
    print(x)
elif y < z < x:
    print(z)
elif z < x < y:
    print(x)
elif z < y < x:
    print(y)
    
