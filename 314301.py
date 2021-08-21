import sys

def volteo(pila:list, n:int):
    
    return pila[n::-1]+pila[n+1:len(pila)]

def esta_ordenado(pila:list):
    for i in range(0,len(pila)-1):
        if pila[i]>pila[i+1]:
            return False
    return True

# for linea in sys.stdin:
#     if linea =="\n":
#         break
#     pila = list(map(int, linea.split()))
#     pila = pila[::-1]

for linea in sys.stdin:
    if linea == "\n":
        break
    pilaW = list(map(int,linea.split()))
    pila = pilaW
    tope = len(pila)
    resultados = ""
    while not esta_ordenado(pila):
        mayor = 0
        i_mayor = 0
        for i in range(0,tope):
            if pila[i]>mayor:
                mayor = pila[i]
                i_mayor = i
            
        tope = tope-1
        if mayor == pila[0]:
            pila = volteo(pila,tope)
            resultados = resultados + str(len(pila)-tope)+" "
            
        elif mayor == pila[tope]:
            pass
        else:
            resultados = resultados + str(len(pila)-i_mayor)+" "+str(len(pila)-tope)+" " 
            
            pila = volteo(pila,i_mayor)
            pila = volteo(pila,tope)
            
        
        
    resultados = resultados +"0"
    cadena = ""
    for elem in pilaW:
        cadena = cadena + str(elem)+" "
    cadena = cadena.rstrip()
    print(cadena)
    print(resultados)