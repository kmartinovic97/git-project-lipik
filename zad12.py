#12.Nađite sva ponavljanja ‘stol’ u zadanom stringu zanemarujući velika i mala slova: „U kuhinji je stol. STOL je novi.”

x = "U kuhinji je stol. STOL je novi."

x = x.lower()

counter = x.count('stol')
print(counter)
