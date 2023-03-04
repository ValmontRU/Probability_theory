# Измерены значения IQ выборки студентов, обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

import numpy as np
import scipy.stats as stats

data = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
beta = 0.95

n = len(data)
x = np.mean(data)
var = np.var(data, ddof = 1)
t = stats.t.ppf(beta + (1 - beta) / 2, n - 1)
xlow = x - t * np.sqrt(var / n)
xup = x + t * np.sqrt(var / n)
# (110.55608365158724, 125.64391634841274)