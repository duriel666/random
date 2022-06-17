class Employee:
    name = 'David'
    salary = 55000
    designation = 'Marketing Head'


class Details:
    name = 'Sam'
    age = 24


e = Employee()
d = Details()

print('Age of David:', getattr(e, 'age', 56))
# print('Age of David:', getattr(e, 'age')) # prints error
setattr(e, "age", 65)
print('Set age of David:', getattr(e, 'age'))
print('Name before modification:', d.name)
print('Age before modification:', d.age)
setattr(d, 'name', 'Timmy')
setattr(d, 'age', 27)
print('Name after modification:', d.name)
print('Age after modification:', d.age)
