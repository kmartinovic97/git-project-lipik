#19. Omogućite unos dviju vrijednosti u dva navrata korisniku.
#Svaki par vrijednosti zapišite u jedan tuple.
#Zamijenite vrijednosti ovih dvaju tupleova te ispišite rezultat.

lista1 = []
lista2 = []

x, y = input('unesite dvije vrijednosti: ').split()
lista1.append(x)
lista1.append(y)
lista1 = tuple(lista1)

a, b = input('unesite druge dvije vrijednosti: ').split()
lista2.append(a)
lista2.append(b)
lista2 = tuple(lista2)

print('prije zamijene')
print('tuple 1', lista1)
print('tuple 2', lista2)

x = lista1
lista1 = lista2
lista2 = x

print('poslije zamijene')
print('tuple 1', lista1)
print('tuple 2', lista2)


