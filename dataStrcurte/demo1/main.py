# # 解压可迭代对象赋值给多个变量
# a = [1, 21, 1, 1, 1, 12, 2, 2]
# b = set(a)
# print(b)
# direct
from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
json.dumps(d)
for key in d:
    print(key, d[key])

# 怎样在数据字典中执行一些计算操作（求最小值、最大值、排序等等）

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(prices.values(), prices.keys())
max_price = max(zip(prices.values(), prices.keys()))
prices_sorted = sorted(zip(prices.values(), prices.keys()))

print(min_price, max_price, prices_sorted)
