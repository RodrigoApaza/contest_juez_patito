n = int(input())
lista_de_listas = []
respuesta = []
for i in range(0,n):
    num_elem = int(input())
    lista = list(map(int, input().split()))
    lista.sort()
    lista_de_listas.append(lista)

for lista in lista_de_listas:
    salida = ""
    for elemento in lista:
        salida = salida+str(elemento)+" "
    salida = salida.rstrip()
    print(salida)