# Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было.

import numpy as np
import scipy.stats as stats

x1 = np.array([150, 160, 165, 145, 155])
x2 = np.array([140, 155, 150,  130, 135])

stats.wilcoxon(x1, x2)
# WilcoxonResult(statistic=0.0, pvalue=0.0625)
# Т.к. pvalue выше стандартной альфа в 5%, то верна гипотеза H0, т.е. статистически значимых различий нет.