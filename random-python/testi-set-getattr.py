class Employee:
    name = 'David'
    salary = 55000
    designation = 'Marketing Head'


e = Employee()

print('Age of David:', getattr(e, 'age', 56))
print('')
#print('Age of David:', getattr(e, 'age'))


class Details:
    name = 'Sam'
    age = 24


# Create an object of the class
d = Details()

print('Name before modification:', d.name)
print('Age before modification:', d.age)

setattr(d, 'name', 'Timmy')
setattr(d, 'age', 27)

print('Name after modification:', d.name)
print('Age after modification:', d.age)
