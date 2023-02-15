# В первом ящике находится 10 мячей, из которых 7 - белые.
# Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча.
# Какова вероятность того, что все мячи белые?
# Какова вероятность того, что ровно два мяча белые?
# Какова вероятность того, что хотя бы один мяч белый?

from math import factorial

def combinations(n,k):
    return factorial(n) // (factorial(k) * factorial(n - k))

outcome1 = combinations(10, 2)
outcome2 = combinations(11, 2)

occurq11 = combinations(7, 2)
occurq12 = combinations(9, 2)
probq11 = occurq11 / outcome1
probq12 = occurq12 / outcome2
probq1 = probq11 * probq12

occurq31 = combinations(3, 2)
occurq32 = combinations(2, 2)
probq31 = occurq31 / outcome1
probq32 = occurq32 / outcome2
probq3 = 1 - probq31 * probq32

print(probq1)
print(probq3)