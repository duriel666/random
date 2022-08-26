# Kirjoita ratkaisu tähän
x = int(input("Kerrokset: "))
merkit = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(x-1, -1, -1):
    row = ""
    for j in range(x-1, 0+i, -1):
        row += merkit[j]
    row += merkit[i]*i*2
    for j in range(i, x):
        row += merkit[j]
    print(row)
for i in range(1, x):
    row = ""
    for j in range(x-1, 0+i, -1):
        row += merkit[j]
    row += merkit[i]*i*2
    for j in range(i, x):
        row += merkit[j]
    print(row)

# esimerkkivastaus

'''n = int(input("Kerrokset: "))

aakkoset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

vasen = ""    # alaspäin menevä osa
oikea = ""    # ylöspäin menevä osa
k = n-1       # seuraavan merkin kohta aakkosissa
m = 2*n-1     # väliin tulevien merkkien määrä
while k >= 1:
    vasen = vasen+aakkoset[k]
    oikea = aakkoset[k]+oikea
    m -= 2
    print(vasen+aakkoset[k]*m+oikea)
    k -= 1
while k <= n-1:
    print(vasen+aakkoset[k]*m+oikea)
    vasen = vasen[:-1]
    oikea = oikea[1:]
    m += 2
    k += 1'''