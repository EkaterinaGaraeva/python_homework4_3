# 1. Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from decimal import *

def find_pi_BBP_formula(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(1)/(16**k)) * ((Decimal(4)/(8*k+1)) - (Decimal(2)/(8*k+4)) - (Decimal(1)/(8*k+5)) - (Decimal(1)/(8*k+6)))
        k += 1
    return pi

def find_pi_Bellards_formula(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        #pi += (Decimal(-1)**k/(1024**k))*(Decimal(256)/(10*k+1) + Decimal(1)/(10*k+9) - Decimal(64)/(10*k+3) - Decimal(32)/(4*k+1) - Decimal(4)/(10*k+5) - Decimal(4)/(10*k+7) - Decimal(1)/(4*k+3))
        pi += Decimal((-1)**k)/(2**(10*k)) * (- Decimal(2**5)/(4*k+1) - Decimal(1)/(4*k+3) + Decimal(2**8)/(10*k+1) - Decimal(2**6)/(10*k+3) - Decimal(2**2)/(10*k+5) - Decimal(2**2)/(10*k+7) + Decimal(1)/(10*k+9))
        k += 1
    pi = pi * 1/(2**6)
    return pi


d = 10
getcontext().prec = d
print(f'Пи = {find_pi_BBP_formula(d)}')
print(f'Пи = {find_pi_Bellards_formula(d)}')
