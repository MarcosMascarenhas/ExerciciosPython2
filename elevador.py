#Capacidade máxima excedida
def capacidade(entrada, saida):    

#queria que de alguma forma a saída contasse como numero negativo, como posso fazer?

    s= saida
    e= entrada
    elevador= 'pessoas dentro' 'teoriamente um int aqui'
    n= saida + entrada
    capacidade= 1000


    if n <= 1000:
        return 'N'

    if n >1000:
        return 'S'
