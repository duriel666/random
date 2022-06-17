sanalista = [
    "banaani", "maito", "olut", "juusto", "piimä", "mehu", "makkara",
    "tomaatti", "kurkku", "voi", "margariini", "juusto", "makkara",
    "olut", "piimä", "piimä", "voi", "olut", "suklaa"
]


def lukumaarat(lista):
    sanat = {}
    for sana in lista:
        # jos sana ei ole vielä tullut vastaan, alusta avaimen arvo
        if sana not in sanat:
            sanat[sana] = 0
        # kasvata sanan esiintymislukumäärää
        sanat[sana] += 1
    return sanat


# kutsutaan funktiota
print(lukumaarat(sanalista))


def alkukirjaimen_mukaan(lista):
    ryhmat = {}
    for sana in lista:
        alkukirjain = sana[0]
        # alusta alkukirjaimeen liittyvä lista kun kirjain tulee vastaan 1. kerran
        if alkukirjain not in ryhmat:
            ryhmat[alkukirjain] = []
        # lisää sana alkukirjainta vastaavalle listalle
        ryhmat[alkukirjain].append(sana)
    return ryhmat


ryhmat = alkukirjaimen_mukaan(sanalista)

for avain, arvo in ryhmat.items():
    print(f"kirjaimella {avain} alkavat sanat: ")
    for sana in arvo:
        print(sana)
