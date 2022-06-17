a = [1, 2, 3, 4, 5, 2, 3, 4, 3]  # list
b = set(())  # set
c = []
d = a
for i in a:
    b.add(i)  # set takes no duplicates
    c.append(i)
print(a)
print(b)
a.sort()
print(a)
print(id(a), id(b), id(c), id(d))
