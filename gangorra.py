p1, c1, p2, c2 = input().split()
p1= int(p1)
c1= int(c1)
p2= int(p2)
c2= int(c2)

resultado1 = p1 * c1 
resultado2 = p2 * c2


if resultado1 == resultado2:
    print ('0')

elif resultado1 > resultado2:
    print('-1')
else:
    print('1')
