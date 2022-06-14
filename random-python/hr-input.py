# 1 4
#x**3 + x**2 + x + 1

#x, k = map(int, input().split(" "))
#print(eval(input()) == k)

x, result = map(int, ("1 4").split(" "))
print(eval("x**3 + x**2 + x + 1") == result)

x = int(input("Anna x:n arvo: "))
lasku = input("Anna laskutehtävä: ")
print(eval(lasku))

eval(input())

x = int(input("Anna x: "))
print("Tulos: "+str(eval(input("Anna lasku: "))))
