n = int(input())
array = list(map(int, input().split()))

mas_repetido = 0
numero_repeticiones = 0
for elemento in array:
    x = array.count(elemento)
    if x>numero_repeticiones:
        numero_repeticiones = x
        mas_repetido = elemento
print(f"{len(array)-numero_repeticiones}")