n, i, j = map(int, input().split())
valores = list(map(int, input().split()))
resultado = valores[0:i]+sorted(valores[i:j+1])+valores[j+1:len(valores)]
respuesta = ''
for num in resultado:
    respuesta = respuesta+" "+str(num)
print(respuesta.lstrip())