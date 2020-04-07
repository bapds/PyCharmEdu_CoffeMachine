valor = int(input())
anos = 0

while valor <= 700000:
    valor *= 1.071
    anos += 1

print(anos)
