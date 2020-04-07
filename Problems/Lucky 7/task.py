n = int(input())

entradas = []

for _N in range(n):
    entrada = int(input())
    entradas.append(entrada)
for y in entradas:
    if y % 7 == 0:
        print(y ** 2)

