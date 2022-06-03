if __name__ == "__main__":
    x = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    a, b = int(input()), int(input())
    for i in range(a, b):
        if i > 0 and i < 10:
            print(x[i])
        elif i > 9:
            if i % 2 == 0:
                print("even")
            else:
                print("odd")
