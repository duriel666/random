# https://rosettacode.org/wiki/Loops/While
n = 1024
while n > 0:
    print(f'{n:,.0f}')  # , is thousands separator ie 1,000 instead of 1000
    print(int(n))
    n //= 2
