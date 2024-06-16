# 动态规划
# 背景 分割不同的木头去卖钱  每米的价钱不同  如何分割才能获得最大的利润
from collections import defaultdict
from functools import wraps

original_price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 33]
# print(len(original_price))
price = defaultdict(int)
print(price)

for i, p in original_price:
    price[i + 1] = p


def memo(func):
    cache = {}

    @wraps(func)
    def _wrap(n):
        if n in cache:
            result = cache[n]
        else:
            result = func(n)
            cache[n] = result
        return result

    return _wrap

@memo
def r(n):
    max_price, split_point = max(
        [(price[n], 0)] + [()]
    )