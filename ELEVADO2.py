from tkinter import Button


n, c = input().split()
n = int(n)
c = int(c)

apareceu_s = False
elevador = 0
contador = 0
while contador < n:
    contador += 1
    s, e = input().split()
    s = int(s)
    e = int(e)
    elevador = elevador - s + e
    if elevador > c:
        apareceu_s = True

if apareceu_s == True:
    print("S")
else:
    print("N")
