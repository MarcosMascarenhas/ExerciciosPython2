consumo = int(input())
fatura = 0

if consumo > 100:
    acima_de_100 = consumo - 100
    parcial_100 = acima_de_100 * 5
    fatura += parcial_100
    consumo = 100

if consumo > 30:
    acima_de_30 = consumo - 30
    parcial_30 = acima_de_30 * 2
    fatura += parcial_30
    consumo = 30

if consumo > 10:
    acima_de_10 = consumo - 10
    parcial_10 = acima_de_10
    fatura += parcial_10
    consumo = 10

fatura = fatura + 7 

print(fatura)