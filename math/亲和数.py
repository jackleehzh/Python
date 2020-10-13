import math

f = {}
for i in range(1000000):
    a = []
    b = []

    for j in range(1, int(math.sqrt(i) + 1)):
        if i % j == 0:
            a.append(j)
            if j > 1:
                a.append(int(i / j))

    d = 0
    for c in a:
        d += c

    for j in range(1, int(math.sqrt(d) + 1)):
        if d % j == 0:
            b.append(j)
            if j > 1:
                b.append(int(d / j))

    e = 0
    for c in b:
        e += c

    if e == i and i != d and (f == {} or i not in f.keys() and i not in f.values()):
        f[i] = d
        print(i, d, "是亲和数。")
        print(i, a)
        print(d, b)


