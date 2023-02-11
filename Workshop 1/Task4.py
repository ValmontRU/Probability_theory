# В лотерее 100 билетов. Из них 2 выигрышных.
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

from math import factorial

def combinations(n,k):
    return factorial(n) // (factorial(k) * factorial(n - k))

outcome = combinations(100, 2) # Общее число исходов (взять 2 билета из 100) = 4950

occur = combinations(2, 2) # Число благоприятных исходов (взять 2 выигрышных билета из 2) = 1
prob = occur / outcome # Вероятность ~ 0,02%