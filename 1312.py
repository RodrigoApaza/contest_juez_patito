import sys
for linea in sys.stdin:
    if linea =="\n":
        break
    conjunto = sorted(list(set(map(int, input().split()))))
    if len(conjunto)<3:
        print(-1)
    else:
        print(conjunto[2])