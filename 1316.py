import sys
for entrada in sys.stdin:
    if entrada =='\n':
        break
    lista_a = list(map(int, input().split()))
    lista_b = list(map(int, input().split()))
    lista_a.sort()
    lista_b = sorted(lista_b, reverse=True)
    print(sum([lista_a[i]*lista_b[i] for i in range(0,len(lista_a))]))