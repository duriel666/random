lista = [5, 2, 3, 1, 4]

lista.append(6)
lista.append(2)

suurin = max(lista)
pienin = min(lista)
summa = sum(lista)
lista2 = sorted(lista)

print("Pienin:", pienin)
print("Suurin:", suurin)
print("Summa:", summa)
print("Lista: ", lista)
print("Järjestettynä: ", lista2)
print("Listan pituus: ", len(lista))


def mediaani(lista: list):
    jarjestetty = sorted(lista)
    keskikohta = len(jarjestetty) // 2
    return jarjestetty[keskikohta]


print("Mediaani: ", mediaani(lista))
