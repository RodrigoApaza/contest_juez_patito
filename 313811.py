texto = input()
array = []
for i in range(0, len(texto)):
    array.append(texto[i:len(texto)])
array.sort()

for elem in array:
    print(elem)