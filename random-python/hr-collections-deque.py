from collections import deque
d = deque()
for _ in range(int(input())):
    inp = input().split()
    getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
    '''if len(inp) > 1:
        getattr(d, inp[0])(inp[1])
    else:
        getattr(d, inp[0])'''
print(*[item for item in d])
