n = int(input())
for i in range(n):
    try:
        x, y = map(int, input().split())
        print(x//y)
    except BaseException as e:
        print("Error Code:", e)
