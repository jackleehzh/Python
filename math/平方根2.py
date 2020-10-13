a = 123456
b = str(a)
c = list(b)

d = int(str(c[0]))
e = 1

if len(c) % 2 == 0:
    d = int(str(c[0]) + str(c[1]))
    e = 2

print(d)

f = 1
g = []
for i in range(2, 10):
    if i ** 2 < d < (i + 1) ** 2:
        f = i
g.append(f)

for i in range(e, len(c), 2):
    for j in range(0, 10):


        if j ** 2 < d < (j + 1) ** 2:
            f = j