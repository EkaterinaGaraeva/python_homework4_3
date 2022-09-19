# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from task004 import polynomial
from task004 import generate_terms
import re

def write_in_files():
    pow = int(input("Введите степень многочлена (целое число от 0 до 100): "))
    result1 = polynomial(pow)
    result2 = polynomial(pow)
    with open("file1.txt", "w") as f:
        f.write(result1)
    with open("file2.txt", "w") as f:
        f.write(result2)

def read_files():
    with open('file1.txt', 'r', encoding='utf-8') as f1:
        s1 = f1.readline()
    with open('file2.txt', 'r', encoding='utf-8') as f2:
        s2 = f2.readline()
    print(s1)
    print(s2)
    return s1, s2

def sum_polynomials(s1, s2):
    s1 = s1.replace(" = 0", "")
    regex_s1 = re.compile("(\\*x )|(\\*x)")
    s1 = regex_s1.sub("", s1)
    regex_s1 = re.compile("\\^. ")
    s1 = regex_s1.sub("", s1)
    list_s1 = s1.split("+ ")
    s2 = s2.replace(" = 0", "")
    regex_s2 = re.compile("(\\*x )|(\\*x)")
    s2 = regex_s2.sub("", s2)
    regex_s2 = re.compile("\\^. ")
    s2 = regex_s2.sub("", s2)
    list_s2 = s2.split("+ ")
    list_s = []
    for i in range(len(list_s1)):
        list_s.append(int(list_s1[i])+int(list_s2[i]))
    list_s.reverse()
    terms = [generate_terms(c, p)
             for (p, c) in enumerate(list_s) if c != 0]
    return " + ".join(terms[::-1]) + " = 0"


write_in_files()
str1, str2 = read_files()
# sum_polynomials(str1, str2)
res = sum_polynomials(str1, str2)
print(res)
with open("file_sum.txt", "w") as f:
    f.write(res)
