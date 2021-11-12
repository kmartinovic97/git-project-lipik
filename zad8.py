#8 Unesi neki nasumični broj kojeg ćeš uzeti kao vrijednost duljine liste u koju se trebaju spremiti vrijednosti od 0 do 1001.
#	Ispiši sljedeće vrijednosti na ekran:
#		a) medijan
#		b) mod
#		c) aritmetičku vrijednost
#		d) sve brojeve koji se u definiranoj listi nalaze ispred vrijednosti koju smo izračunali kao medijan navedene liste
#		e) sve brojeve koji su manji od vrijednosti koju smo izračunali kao medijan navedene liste

#	*Bonus: Napravite novu listu koja sadrži samo vrijednosti koje su za 10% veće ili manje od aritmetičke sredine
import math
lista = []
lista_manji = []

duljina_liste = int(input('Unesi duljinu liste: '))

#unos u listu
for i in range(0, duljina_liste):
    elem = int(input('Unesi element: '))
    while elem not in range(0, 1001):
        elem = int(input('Element ne zadovoljava uvijete, Unesi element: '))
    lista.append(elem)
print('lista = ', lista)



#medijan - centralna vrijednost
#duljina neparna
#indexi pocinju od 0, pa mi za centralni element  od duljine 5 treba 2 a ne 3
if duljina_liste%2!=0:
    y = math.floor(duljina_liste/2)
    medijan = lista[y]
    print('medijan je ', medijan)
    for i in lista:
        if i < medijan:
            lista_manji.append(i)

#parna duljina
elif duljina_liste%2==0:
    x = int(duljina_liste/2)
    y = x - 1
    avg2 = ((lista[y]+lista[x])/2)
    print('medijan je ', avg2)
    for i in lista:
        if i < avg2:
            lista_manji.append(i)




#modus
from collections import Counter


def most_frequent(lista):
    occurence_count = Counter(lista)
    return occurence_count.most_common(1)[0][0]



print('modus je ', most_frequent(lista))


#c) aritmetičku vrijednost
suma = 0
for elem in lista:
    suma = suma + elem
avg = suma/duljina_liste
print('aritmeticka vrijednost je', avg)

#d) sve brojeve koji se u definiranoj listi nalaze ispred vrijednosti koju smo izračunali kao medijan navedene liste

print('brojevi koji se nalaze ispred medijana', lista[0:y])

#sortiranje liste
#lista = sorted(lista)
#print(lista)
#print(medijan)

#e) sve brojeve koji su manji od vrijednosti koju smo izračunali kao medijan navedene liste




print('brojevi manji od medijana', lista_manji)

