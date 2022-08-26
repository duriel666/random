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
