a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

receita_a = 2
receita_b = 3
receita_c = 5

quantidade_a = a//receita_a
quantidade_b = b//receita_b
quantidade_c = c//receita_c


if quantidade_a == quantidade_b and quantidade_c == quantidade_a:
    print(quantidade_a)
else:
    if quantidade_a <= quantidade_b and quantidade_a <= quantidade_c:
        print(quantidade_a)
    elif quantidade_b <= quantidade_a and quantidade_b <= quantidade_c:
        print (quantidade_b)    
    elif quantidade_c <= quantidade_a and quantidade_c <= quantidade_b:
        print (quantidade_c)
