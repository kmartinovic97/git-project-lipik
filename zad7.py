#7. Ispiši vrijednost broja Pi na 4 decimalna mjesta, kvadriraj taj broj te ga podijeli s racionalnim brojem odabranim
# od strane korisnika (input funkcija) i ispiši rezultat.

import math
pi = math.pi
pi = format(pi, '.4f')
print(pi)
pi = float(pi)

x = float(input('unesi broj: '))

print((pi*pi)/x)


