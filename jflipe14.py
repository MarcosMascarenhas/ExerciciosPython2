#input_linha = input()
#input_splitted = input_linha.split()
#input_splitted = input().split()
#p, r = input_splitted


p, r = input().split()
p = int(p)
r = int(r)

if p == 1:
    if r == 1:
        print("A")
    else:
        print("B")
else:
    print("C")








def flipper(p, r):
    if p == 1:
        if r == 1:
            return "A"
        else:
            return "B"
    else:
        return "C"

p, r = input().split()
p = int(p)
r = int(r)
print(flipper(p, r))















