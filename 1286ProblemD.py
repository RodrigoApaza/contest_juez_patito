n = int(input())
resultados = []
for i in range(0,n):
    lista = input().split(" ")
    contador_consecutivos = 0
    for i in range(0,len(lista)-1):
        if int(lista[i])==0:
            break
        if int(lista[i])<int(lista[i+1]):
            contador_consecutivos= contador_consecutivos+1
    resultados.append(contador_consecutivos)

for r in resultados:
    print(r)