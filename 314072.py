import sys

for linea in sys.stdin:
    if linea =="\n":
        break
    n = int(linea)
    lista = list(map(int,input().split()))

    lista = sorted(lista)
    distancia = 0
    for i in range(0,len(lista)-1):
        distancia = distancia + (lista[i+1]-lista[i])
    print(distancia)    
