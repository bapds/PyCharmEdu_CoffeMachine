#  Posted from EduTools plugin
ent = ''
bares = []
sub_lista = []
sub_lista2 = []
posi = 0

while ent != 'MEOW':
    ent = input()
    if ent == 'MEOW':
        break
    bares.append(ent.split())

for n in bares:
    for m in n:
        try:
            sub_lista.append(int(m))

        except:
            sub_lista2.append(m)
            continue


mais_gatos = max(sub_lista)
posi = sub_lista.index(mais_gatos)

print(sub_lista2[posi])
