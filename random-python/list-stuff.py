a = [1, 2, 3, 4, 5, 2, 3, 4, 3]  # list
b = set(())  # set
for i in a:
    b.add(i)  # set takes no duplicates
print(a)
print(b)
a.sort()
print(a)
