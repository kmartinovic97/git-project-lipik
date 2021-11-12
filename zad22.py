#22. Napravite funkciju koja prima brojeve i vraća redom:
#	a) umnožak tih brojeva
#	b) zbroj tih brojeva
#	c) poredak po veličini (descending)
#	d) tuple prostih brojeva koji su unešeni
#	e) tuple parnih brojeva koji su unešeni
#	*uzmite rezultate te funkcije te ih zapišite u file def_rez.txt

def funk():
    n = int(input('Koliko brojeva zelite unjeti: '))
    i = 0
    umnozak = 1
    zbroj = 0
    lista = []
    lista_prosti = []
    lista_parnih = []

    while i < n:
        x = int(input('unesi broj: '))
        lista.append(x)
        i += 1

    for elem in lista:
        umnozak = umnozak * elem
        zbroj = zbroj + elem
        if elem%2 == 0:
            lista_parnih.append(elem)

    for elem in lista:
        if elem > 1:
            for i in range(2, elem):
                if (elem % i) == 0:
                    break
            else:
                lista_prosti.append(elem)

    tuple_liste_prostih = tuple(lista_prosti)
    tuple_liste_parnih = tuple(lista_parnih)



    print('zbroj je: ', zbroj, 'umnozak je: ', umnozak)
    print(sorted(lista, reverse=True))
    print(tuple_liste_prostih)
    print(tuple_liste_parnih)


funk()

