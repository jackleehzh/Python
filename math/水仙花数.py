for i in range(100, 10000000, 1):
    b = []
    a = i
    while a > 9:
        b.append(a % 10)
        a = int(a / 10)
    b.append(a)
    c = 0
    d = len(b)
    #print(d)
    for e in b:
        c += e ** d
    #print(i, c)
    if c == i:
        print(i)