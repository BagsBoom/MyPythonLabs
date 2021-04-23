import random
import numpy

array = [random.randint(0,25) for i in range(10)]
print(array)

def quicksort():
    """Quick sorting of the list."""
    array.sort()
    print(array)

def search_in_array():
    """Search element by value in list."""
    value = int(input("Уведіть значення: "))
    print("Статус значення: ",value in array)


def search_values_in_array():
    """Search sequences of elements"""
    value = int(input("Уведіть кількість елементів послідовності: "))
    values = []
    for i in range(value):
        values.append(int(input("Уведіть число: ")))
    print(values)
    #print(set(values).issubset(array))
    print("Статус операції: ",all(i in array for i in values))

def min_five():
    """First five min elements"""
    array.sort()
    print(array[:5])

def max_five():
    """First five max elements"""
    array.sort()
    print(array[5:10])

def average():
    """Arithmetic mean for elements in the list"""
    print("Середнє арифметичне:",numpy.mean(array))

def without_repeats():
    """Non-repeat list"""
    print("Список без повторень: ",list(set(array)))
