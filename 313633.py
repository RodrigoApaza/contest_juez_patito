
n = int(input())
for i in range(0,n):
    materiales = list(map(int, input().split()))
    c_piedra = materiales[0]
    palitos = materiales[1]
    picos = 0
    while True:
        if palitos -2 >=0 and c_piedra -3>=0:
            picos = picos +1
            palitos=palitos-2
            c_piedra =c_piedra-3
        else:
            print(f"{picos} {c_piedra+palitos}")
            break
    