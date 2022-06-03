def swap_case(s):
    s2 = ""
    for x in s:
        if x.isupper():
            s2 += x.lower()
        elif x.islower():
            s2 += x.upper()
        else:
            s2 += x
    return s2


if __name__ == '__main__':
    print(swap_case("Testi!!"))
