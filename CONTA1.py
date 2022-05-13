consumo = int(input())
fatura = 0

#print("INICIO DO CODIGO - FATURA = " + str(fatura) + " CONSUMO = " + str(consumo))

if consumo > 100:
    #print("CONSUMO É ACIMA DE 100, VOU FAZER PARANAUES")
    consumo_acima_de_100 = consumo - 100
    fatura_acima_de_100 = consumo_acima_de_100 * 5
    fatura += fatura_acima_de_100
    consumo = 100

if consumo > 30:
    #print("CONSUMO É ACIMA DE 30, VOU FAZER PARANAUES")
    consumo_acima_de_30 = consumo - 30
    fatura_acima_de_30 = consumo_acima_de_30 * 2
    fatura += fatura_acima_de_30
    consumo = 30

#print("DEPOIS DOS PARANAUE DE 30 - FATURA = " + str(fatura) + " CONSUMO = " + str(consumo))

if consumo > 10:
    #print("CONSUMO É ACIMA DE 10, VOU FAZER PARANAUES")
    consumo_acima_de_10 = consumo - 10
    fatura_acima_de_10 = consumo_acima_de_10 * 1
    fatura += fatura_acima_de_10
    consumo = 10
    
#print("DEPOIS DOS PARANAUE DE 10 - FATURA = " + str(fatura) + " CONSUMO = " + str(consumo))

fatura += 7

print(fatura)
