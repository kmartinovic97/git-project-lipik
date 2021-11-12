#21. Napišite funkciju koja prima isključivo stringove i vraća tuple pojedinačnih charactera, uključujući i razmake.

def string_funkcija():
    string = str(input('unesi string: '))
    t1 = tuple(string)
    print(t1)

string_funkcija()
