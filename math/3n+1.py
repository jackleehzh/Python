l = input().split()
a = ll(l[0])
b = int(l[1])
c = 0


def get_result(e):
    d = 1
    while e != 1:
        if e % 2 == 0:
            e /= 2
        else:
            e += 2 * e + 1
        d += 1
    return d


for i in range(a, b + 1):
    d = get_result(i)
    if d > c:
        c = d

print('%d %d %d' % (a, b, c))
