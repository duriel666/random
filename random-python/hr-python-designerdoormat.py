xy = "11 33"
spot = xy.find(" ")
y = xy[:spot]
x = xy[spot+1:]
for i in range(int(y)//2):
    print("-"*((int(x)//2)-1-(i*3))+".|."*i +
          ".|."+".|."*i+"-"*((int(x)//2)-1-(i*3)))
print("-"*((int(x)//2)-3)+"WELCOME"+"-"*((int(x)//2)-3))
for i in range((int(y)//2)-1, -1, -1):
    print("-"*((int(x)//2)-1-(i*3))+".|."*i +
          ".|."+".|."*i+"-"*((int(x)//2)-1-(i*3)))
