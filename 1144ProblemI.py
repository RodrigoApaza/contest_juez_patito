def busqueda_bin(arreglo, busqueda, izquierda, derecha):
    if izquierda > derecha:
        return -1
    indiceDelElementoDelMedio = (izquierda + derecha) // 2
    elementoDelMedio = arreglo[indiceDelElementoDelMedio]
    if elementoDelMedio == busqueda:
        return indiceDelElementoDelMedio
    if busqueda < elementoDelMedio:
        return busqueda_bin(arreglo, busqueda, izquierda, indiceDelElementoDelMedio - 1)
    else:
        return busqueda_bin(arreglo, busqueda, indiceDelElementoDelMedio + 1, derecha)


def criba(n):
    primes = []
    isPrime = [1 for i in range(n)]
    isPrime[0] = isPrime[1] = 0

    for i in range(n):
        if isPrime[i]:
            primes.append(i)
            h = 2
            while i*h < n:
                isPrime[i*h] = 0
                h += 1

    return primes


resultados = []
lista = criba(1000100)

n = int(input())
valores = []
for i in range(0,n):
    valores.append(int(input()))


for valor in valores:
    if(busqueda_bin(lista,valor,0,len(lista)))==-1:
        for i in range(0,len(lista)-2):
            a = lista[i]
            b = lista[i+1]
            if a<valor and b>valor:
                resultados.append(a+b)
    else:
        indice = busqueda_bin(lista,valor,0,len(lista))
        resultados.append(lista[indice-1]+lista[indice+1])
        
        
        

for r in resultados:
    print(r)

