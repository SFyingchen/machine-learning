import numpy as np
import matplotlib.pyplot as plt
import random
from icecream import ic


def func(x):
    return 10 * x ** 2 + 32 * x + 9


def gradient(x):
    return 20 * x + 32


# 创建一个从-10到10的等差数列，并赋值给变量x，用于后续在图上绘制完整的函数曲线
# 默认情况下，这个数列包含 50 个元素（除非明确指定了其他数量），并且这些元素在 -10 和 10 之间均匀分布
x = np.linspace(-10, 10)

steps = []

x_star = random.choice(x)

alpha = 1e-3

for i in range(100):
    x_star = x_star - gradient(x_star) * alpha

    steps.append(x_star)

    ic(x_star, func(x_star))

fig, ax = plt.subplots()
ax.plot(x, func(x))

for i, s in enumerate(steps):
    ax.annotate(str(i + 1), (s, func(s)))

plt.show()
