n = int(input())
lista = {}
for i in range(n):
    x = input().split(" ")
    hinta = int(x[-1])
    tavara = " ".join(x[:-1])
    if tavara in lista:
        lista[tavara] += hinta
    else:
        lista[tavara] = hinta
for x, y in lista.items():
    print(x, y)
