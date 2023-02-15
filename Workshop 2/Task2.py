# Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек.
# Какова вероятность, что ни одна из них не перегорит в первый день?
# Какова вероятность, что перегорят ровно две?

from math import factorial

def poisson(n,m,p,e):
    return (n * p) ** m // factorial(m) * e ** -(n * p)

prob1 = poisson(5000, 0, 0.0004, 2.71828)
prob2 = poisson(5000, 2, 0.0004, 2.71828)

print(prob1)
print(prob2)