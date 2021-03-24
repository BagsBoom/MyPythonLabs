import math
x = int(input("Уведіть x: "))
y =  int(input("Уведіть y: "))
z = math.cos(x)**2 + math.sin(y)**2 + 1/4*math.sin(x*2)**2 - 1
print("Z = ", z)
