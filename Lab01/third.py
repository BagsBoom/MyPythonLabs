import random
from functools import reduce

array = []
for i in range(0,25):
    x = random.randint(0,25)
    array.append(x)
print("Масив: ",array)
print("Мінімальний елемент: ",min(array))
unpaired = [n for n in array if n % 2]
print("Добуток ненульових непарних елементів: ",reduce(lambda x, y: x * y, unpaired))
array.reverse()
print(array)