# Вероятность того, что стрелок попадёт в мишень, выстрелив один раз, равна 0.8.
# Стрелок выстрелил 100 раз.
# Найдите вероятность того, что стрелок попадёт в цель ровно 85 раз.

from math import factorial

def bernoulli(n,k,p):
    return factorial(n) // (factorial(k) * factorial(n - k)) * p ** k * (1 - p) ** (n - k)

prob = bernoulli(100, 85, 0.8)

print(prob)