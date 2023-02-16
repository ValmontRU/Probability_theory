# Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean)
# среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.

data = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

n = len(data)
mean = sum(data) / n
variance = sum([(x - mean) ** 2 for x in data]) / n
unbiasedVariance = sum([(x - mean) ** 2 for x in data]) / (n - 1)
deviation =  variance ** 0.5

print(mean)
print(variance)
print(unbiasedVariance)
print(deviation)