# Descripción
# Se dice que dos fracciones son iguales si el numerador y el denominador de las dos fracciones son iguales, por ejemplo 33/15 es igual a 11/5 ya que simplifícando 33/15 tenemos 11/5 que es igual a la segunda fracción.
# Dado dos fracciones determinar si estos son iguales.

# Entrada
# La entrada viene dada por varios casos en una misma entrada. Cada linea de la entrada representa un caso.

# Cada caso consiste en cuatro números enteros los dos primeros n1 y d1 son los valores de la primera fracción siendo n1 el numerador y d1 el denominador, siguen n2 y d2 siendo los valores de la segunda fracción donde n2 es el numerador y d2 el denominador (1<=n1,n2,d1,d2<=1000) la entrada termina cuando n1=d1=n2=d2=0. Es decir, los ultimo 4 numeros de la entrada seran 0's y este caso representa el fin de los datos de entrada y no debe ser procesado.

# Salida
# Imprimir '=' si las fracciones son iguales caso contrario imprimir '!=', sin incluir las comillas

resultados = []
while True:
    lista = []
    lista = input().split(" ")

    for i in range(0,len(lista)):
        lista[i] = int(lista[i])
    if lista[0] ==0 or lista[1]==0 or lista[2]==0 or lista[3]==0:
        break

    factor1 = lista[0]/lista[1]
    factor2 = lista[2]/lista[3]

    if factor1 == factor2:
        resultados.append("=")
    else:
        resultados.append("!=")

for r in resultados:
    print(r)