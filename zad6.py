#6. Unesi jedan nasumični broj.
#Ispiši aritmetičku sredinu onoliko brojeva(0-101) koliko je iznosio uneseni nasumični broj.
#Navedeni broj uzmi kao vrijednost opsega kruga te ispiši vrijednost polumjera navedenog kruga.


import random
import math

x = random.randint(0, 101)
print(x)
zbroj = 0
for i in range(0, x+1):
    zbroj = zbroj + i

avg = zbroj/x
print(avg)

#r = o/ (pi*2)

r = avg / (math.pi*2)
print(r)