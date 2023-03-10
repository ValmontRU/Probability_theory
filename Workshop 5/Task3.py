# Проведите тест гипотезы. Продавец утверждает, что средний вес пачки печенья составляет 200 г.
# Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
# 202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
# Известно, что их веса распределены нормально.
# Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%?
# (Провести двусторонний тест.)

import numpy as np

m = 200
n = 10
data = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])
beta = 0.99

# H0: x = m
# H1: x != m
# Критерий t, т.к. неизвестно отклонение генеральной совокупности
# t табличное ~ 2.821

x = np.mean(data)
# 198.5

dev = np.std(data, ddof=1)
# 4.453463071962462

t = (x - m) / ( dev / n ** 0.5)
# -1.0651074037450896

# 2.821 > |-1.0651074037450896|, следовательно верна гипотеза H0