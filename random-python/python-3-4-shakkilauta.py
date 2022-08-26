def shakkilauta(a):
    k = 1
    mjono = ""
    for x in range(0, a):
        for y in range(0, a):
            if k == 1:
                mjono += "1"
            else:
                mjono += "0"
            k *= -1
        if a % 2 == 0:
            k *= -1
        print(mjono)
        mjono = ""


def shakkilauta2(koko):  # mallivastaus
    i = 0
    while i < koko:
        if i % 2 == 0:
            rivi = "10"*koko
        else:
            rivi = "01"*koko
        # poistetaan rivin lopusta ylimääräiset merkit
        print(rivi[0:koko])
        i += 1


if __name__ == "__main__":
    shakkilauta(4)
    shakkilauta2(4)
