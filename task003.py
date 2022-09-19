# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

from random import randint

def list_of_non_repeating_elements(list_of_numbers):
    list_of_elements = []
    for i in list_of_numbers:
        if i not in list_of_elements:
            list_of_elements.append(i)
    list.sort(list_of_elements)
    return list_of_elements

def list_of_non_repeating_elements2(list_of_numbers):
    return set(list_of_numbers)


lst = [randint(0, 9) for i in range(10)]
print(lst)
print(list_of_non_repeating_elements(lst))
print(list_of_non_repeating_elements2(lst))
