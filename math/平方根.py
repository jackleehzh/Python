a = 1
b = 1
c = int(input('输入一个数求它的平方根：'))
while True:
    if a ** 2 < c:
        a += b
    elif a ** 2 > c:
        a -= b
        b /= 2
    else:
        break

    if a == a + b:
        break

print(str(c) + '的平方根是：', a)
