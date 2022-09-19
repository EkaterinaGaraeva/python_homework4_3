# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def generate_terms(coef: int, pow: int) -> str:
    if pow == 0:
        return f"{coef}"
    elif pow == 1:
        return f"{coef}*x"
    else:
        return f"{coef}*x^{pow}"

def polynomial(power):
    coefficients = [randint(0, 100) for _ in range(power + 1)]
    # print(coefficients)
    terms = [generate_terms(c, p)
             for (p, c) in enumerate(coefficients) if c != 0]
    return " + ".join(terms[::-1]) + " = 0"

def write_polynomial(result):
    with open("file.txt", "w") as f:
        f.write(result)

if __name__ == "__main__":
    k = int(input("Введите степень многочлена (целое число от 0 до 100): "))
    res = polynomial(k)
    print(res)
    write_polynomial(res)
