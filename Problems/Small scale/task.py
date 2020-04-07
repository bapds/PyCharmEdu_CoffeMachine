ent = ''

lista = []

while ent != '.':
  ent = input()

  if ent == '.':
    break

  lista.append(float(ent))

print(min(lista))
