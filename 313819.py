def suma_digitos(numero:int):
    suma = 0
    while(numero!=0):
        suma = suma + numero % 10
        numero = numero //10
    return suma
lista = []
valor = int(input())
lista = list(map(int, input().split()))

for i in range(0,len(lista)-1):
    for j in range(i+1,len(lista)):
        if suma_digitos(lista[i])>suma_digitos(lista[j]):
            n = lista[i]
            lista[i] = lista[j]
            lista[j] = n
        elif suma_digitos(lista[i]) == suma_digitos(lista[j]):
            if lista[i]>lista[j]:
                n = lista[i]
                lista[i] = lista[j]
                lista[j] = n

cadena = ""
for elem in lista:
    cadena = cadena+str(elem)+" "

print(cadena.rstrip())
