import math

# 求某个整数区间中相对于某个模的剩余个数
a = int(input('下限'))
b = int(input('上限'))
c = int(input('模'))

e = 0

d = a % c

if d != 0:
    d = b % c

if d == 0:
    e += 1
    e += math.floor((b - a) / c)
else:
    e += math.floor((b - a + 1) / c)

print(e)
