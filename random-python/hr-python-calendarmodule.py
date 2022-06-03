import calendar


m, d, y = 8, 5, 2015  # map(int, input().split())
day = calendar.weekday(y, m, d)
print(calendar.day_name[day].upper())
