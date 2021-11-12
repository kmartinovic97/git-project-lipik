#4. Napišite program koji će u varijable a i b spremiti dva dvoznamenkasta broja. U varijablu a pohranite zadnju
# znamenku broja koji se nalazi u varijabli b, a u varijablu b pohranite zadnju znamenku broja koja se nalazi u
# varijabli a. Ispišite sadržaj varijabli a i b.

a = int(input('unesi 1. dvoznamenkasti broj: '))

while a not in range(10, 100):
    a = int(input('nije dvoznamenkasti broj, probaj ponovo: '))

b = int(input('unesi 2. dvoznamenkasti broj: '))
while b not in range(10, 100):
    b = int(input('nije dvoznamenkasti broj, probaj ponovo: '))


zadnja_znamenka_a = a%10
zadnja_znamenka_b = b%10

a = zadnja_znamenka_b
b = zadnja_znamenka_a

print(f'zadnja znamenka varijable b je {a}, a zadnja znamenka varijable a je {b}')
