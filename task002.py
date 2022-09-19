# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def list_of_all_multipliers(n):
    list_of_multipliers = []
    for i in range(2, n + 1):
        if (int(n % i) == 0):
            list_of_multipliers.append(i)
    if len(list_of_multipliers) == 1:
        list_of_multipliers = [n]
    return list_of_multipliers


def list_of_simple_multipliers(list_of_multipliers):
    simple_multipliers = []
    for j in list_of_multipliers:
        if (len(list_of_all_multipliers(j)) == 1):
            simple_multipliers.append(j)
    return simple_multipliers


n = 46
print(f'Все множители числа N = {n} (кроме 1): {list_of_all_multipliers(n)}')
print(f'Простые множители числа N = {n}: {list_of_simple_multipliers(list_of_all_multipliers(n))}')
