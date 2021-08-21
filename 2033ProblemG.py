# Descripción
# Se ha pedido hacer una bandera muy grande. Cada persona trajo cortes de tela para coser que son todos del mismo tamaño. Cada color esta representado por r,a,v que representan rojo, amarillo, y verde respectivamente.

# La bandera debe tener la misma cantidad de cada uno de los colores.

# Entrada
# La entrada consiste de varios casos de prueba. La primera línea  consiste de un número que indica el número de casos de prueba. Cada caso de prueba es una cadena que contiene caracteres r,a,v.

# Salida
# Por cada caso de prueba escriba el tamaño más grande de bandera que puede coser.

# Ejemplo Entrada
# 4
# rrvaaavaaaa
# rrrvraavrvvavv
# arvvrvaaarvaavarravar
# avvarrrraavvvraavavrvvv
# Ejemplo Salida
# 2
# 3
# 6
# 6
def menor(a:int, b:int):
    if a<b:
        return a
    return b

resultados = []
n = int(input())

for i in range(0,n):
    telas = input()
    r = telas.count("r")
    a = telas.count("a")
    v = telas.count("v")
    min = menor(r,menor(a,v))
    resultados.append(min)

for r in resultados:
    print(r)