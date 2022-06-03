# https://rosettacode.org/wiki/Loops/Break
import random

while True:
    r = random.randrange(0, 20)
    print(r)
    if r == 10:
        break
