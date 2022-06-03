# 9 and 1 2 3 4 5 6 7 8 9
# 9 and 10 1 2 3 11 21 55 6 8
_, a = input(), set(input().split())
_, b = input(), set(input().split())
print(a,b)
print(len(a.union(b)))
