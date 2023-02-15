# Монету подбросили 144 раза. Какова вероятность, что орёл выпадет ровно 70 раз?

from math import factorial

def bernoulli(n,k,p):
    return factorial(n) // (factorial(k) * factorial(n - k)) * p ** k * (1 - p) ** (n - k)

prob = bernoulli(144, 70, 0.5)

print(prob)