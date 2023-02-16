# В первом ящике находится 8 мячей, из которых 5 - белые.
# Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4.
# Какова вероятность того, что 3 мяча белые?

# Искомое - сумма вероятностей следующих раскладов (белые шары из 1-го ящика, белые шары из 2-го ящика):
# (0, 3) + (1, 2) + (2, 1)

# Расклад №1: (--) И (+++-) ИЛИ (++-+) ИЛИ (+-++) ИЛИ (-+++) 0.01515151515151515
prob1 = (3/8 * 2/7) * (5/12 * 4/11 * 3/10 * 7/9) \
      + (3/8 * 2/7) * (5/12 * 4/11 * 7/10 * 3/9) \
      + (3/8 * 2/7) * (5/12 * 7/11 * 4/10 * 3/9) \
      + (3/8 * 2/7) * (7/12 * 5/11 * 4/10 * 3/9)

# Расклад №2: (+-) ИЛИ (-+) И (++--) ИЛИ (+-+-) ИЛИ (+--+) ИЛИ (-+-+) ИЛИ (-++-) ИЛИ (--++) 0.2272727272727273
prob2 = (5/8 * 3/7) * (5/12 * 4/11 * 7/10 * 6/9) \
      + (5/8 * 3/7) * (5/12 * 7/11 * 4/10 * 6/9) \
      + (5/8 * 3/7) * (5/12 * 7/11 * 6/10 * 4/9) \
      + (5/8 * 3/7) * (7/12 * 5/11 * 6/10 * 4/9) \
      + (5/8 * 3/7) * (7/12 * 5/11 * 4/10 * 6/9) \
      + (5/8 * 3/7) * (7/12 * 6/11 * 5/10 * 4/9) \
      + (3/8 * 5/7) * (5/12 * 4/11 * 7/10 * 6/9) \
      + (3/8 * 5/7) * (5/12 * 7/11 * 4/10 * 6/9) \
      + (3/8 * 5/7) * (5/12 * 7/11 * 6/10 * 4/9) \
      + (3/8 * 5/7) * (7/12 * 5/11 * 6/10 * 4/9) \
      + (3/8 * 5/7) * (7/12 * 5/11 * 4/10 * 6/9) \
      + (3/8 * 5/7) * (7/12 * 6/11 * 5/10 * 4/9)

# Расклад №3: (++) И (+---) ИЛИ (-+--) ИЛИ (--+-) ИЛИ (---+) 0.1262626262626263
prob3 = (5/8 * 4/7) * (5/12 * 7/11 * 6/10 * 5/9) \
      + (5/8 * 4/7) * (7/12 * 5/11 * 6/10 * 5/9) \
      + (5/8 * 4/7) * (7/12 * 6/11 * 5/10 * 5/9) \
      + (5/8 * 4/7) * (7/12 * 6/11 * 5/10 * 5/9)

prob = prob1 + prob2 + prob3 # 0.36868686868686873