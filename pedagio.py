l, d = input().split()
k, p = input ().split()
l= int(l)
d= int (d)
k= int (k)
p= int (p)

qtdped= l//d
custoped= p*qtdped
custokm= l*k

total = custoped + custokm
print(total)