# 1 4
#x**3 + x**2 + x + 1

#x, k = map(int, input().split(" "))
#print(eval(input()) == k)

x, result = map(int, ("1 4").split(" "))
print(eval("x**3 + x**2 + x + 1") == result)

# extra juttuja jotka ei liity tehtävään

x = int(input("Anna x:n arvo: "))
lasku = input("Anna laskutehtävä: ")
print(eval(lasku))

eval(input())

x = int(input("Anna x: "))
print("Tulos: "+str(eval(input("Anna lasku: "))))

a, b, c = map(int, input("Syötä a b c: ").split(" "))
print("Tulos: x="+str(eval("(-b+((b**2-4*a*c)**0.5))/(2*a)")) +
      " tai x="+str(eval("(-b-((b**2-4*a*c)**0.5))/(2*a)")))
