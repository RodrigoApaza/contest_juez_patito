def es_ordenado(lista:list):
    for i in range(0,len(lista)-1):
        if lista[i]>lista[i+1]:
            return False
    return True

n = int(input())

for i in range(n):
    longitud = int(input())
    tren = list(map(int, input().split()))
    con_pasos = 0
    while not(es_ordenado(tren)):
        for i in range(0,len(tren)-1):
            if tren[i]>tren[i+1]:
                a = tren[i]
                tren[i] = tren[i+1]
                tren[i+1] = a
                con_pasos = con_pasos + 1
                break
    print(con_pasos)
    