import sys
for linea in sys.stdin:
    if linea=="\n":
        break
    n = int(linea)
    lista = list(map(int, input().split()))
    if len(lista)==1:
        print(lista[0])
    else:
        if len(lista)%2==0:
            print("-1")
        else:
            lista.sort()
            mediana = len(lista)//2
            if lista[mediana]>lista[mediana-1] and lista[mediana]<lista[mediana+1]:
                print(lista[mediana])
            else:
                print("-1")