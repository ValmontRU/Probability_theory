# В университет на факультеты A и B поступило равное количество студентов,
# а на факультет C студентов поступило столько же, сколько на A и B вместе.
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9.
# Студент сдал первую сессию. Какова вероятность, что он учится:
# a). на факультете A б). на факультете B в). на факультете C?

pA = 1/4 * (0.8 + 0.7) + 1/2 * 0.9
p1 = (1/4 * 0.8) / pA # 0.24242424242424246
p2 = (1/4 * 0.7) / pA # 0.21212121212121213
p3 = (1/2 * 0.9) / pA # 0.5454545454545455