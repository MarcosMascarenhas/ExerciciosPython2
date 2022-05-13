a,b,c = input().split()
x,y,z = input().split()
a= int(a)
b= int(b)
c= int(c)
x= int(x)
y= int(y)
z= int(z)



largura = x//a
comprimento = y//b
altura = z//c

conteiners = largura * comprimento * altura

print (conteiners)
