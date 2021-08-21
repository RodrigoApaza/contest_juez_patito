numero = int(input())
resultados = []
for i in range(0,numero):
    cantidad_inicio_fin = input().split(" ")
    cantidad = cantidad_inicio_fin[0]
    inicio = int(cantidad_inicio_fin[1])
    fin = int(cantidad_inicio_fin[2])

    lista = input().split(" ")
    suma = 0
    for i in range(inicio, fin+1):
        suma = suma+int(lista[i])
    resultados.append(suma)
for r in resultados:
    print(r)

    