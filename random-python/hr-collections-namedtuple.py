from collections import namedtuple


x = int(input())
fields = input().split()
total = 0
for i in range(x):
    students = namedtuple("student", fields)
    a, b, c, d = input().split()
    student = students(a, b, c, d)
    total += int(student.MARKS)
print("{:.2f}".format(total/x))
