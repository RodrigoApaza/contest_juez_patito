import sys
for linea in sys.stdin:
    if linea=="\n":
        break
    personas = list(map(int, linea.split()))
    personas.sort()
    equipo1 = []
    equipo2 = []
    while(len(personas)>0):
        equipo1.append(personas.pop())
        if len(personas)>0:
            equipo2.append(personas.pop())
    diferencia = abs(sum(equipo1)-sum(equipo2))
    print(diferencia)