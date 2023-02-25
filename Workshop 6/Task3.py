# Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.

import numpy as np
import scipy.stats as stats

daughters = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
mothers = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
beta = 0.95

x1 = np.mean(daughters)
x2 = np.mean(mothers)
n = len(daughters)
delta = x1 - x2
var1 = np.var(daughters, ddof = 1)
var2 = np.var(mothers, ddof = 1)
var = (var1 + var2) / 2
se = np.sqrt(2 * var / n)
t = stats.t.ppf(beta + (1 - beta) / 2, 2 * (n - 1))
low = delta - t * se
up = delta + t * se
# (-10.068418034506857, 6.268418034506846)