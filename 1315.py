n = input()
linea = input().rstrip()
lista = list(map(int, linea.split(' ')))
a = [str(lista[0]) if x==0 else str(lista[x]-lista[x-1]) for x in range(0,len(lista))]
a = ' '.join(a)
print(a)