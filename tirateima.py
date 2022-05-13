x,y = input('digite as coordenadas da bola').split()
x = int(x)
y = int(y)

semi_quadra_1x= 0 
semi_quadra_2x= 432
semi_quadra_1y= 0 
semi_quadra_2y= 468


if x > semi_quadra_2x or x < semi_quadra_1x:
    print('fora')

elif y > semi_quadra_2y or y < semi_quadra_1y:
    print('fora')

else:
    print('dentro')