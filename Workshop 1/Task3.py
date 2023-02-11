# В ящике имеется 15 деталей, из которых 9 окрашены.
# Рабочий случайным образом извлекает 3 детали.
# Какова вероятность того, что все извлеченные детали окрашены?

from math import factorial

def combinations(n,k):
    return factorial(n) // (factorial(k) * factorial(n - k))

outcome = combinations(15, 3) # Общее число исходов (достать 3 детали из 15) = 455

occur = combinations(9, 3) # Число благоприятных исходов (достать 3 детали из 9 окрашенных) = 84
prob = occur / outcome # Вероятность ~ 18,46%