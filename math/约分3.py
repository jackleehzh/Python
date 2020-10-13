a = int(input('请输入分子：'))
b = int(input('请输入分母：'))

c = a
if a > b:
    c = b

for i in range(2, c + 1):
    while a % i == b % i:
        a /= i
        b /= i

print(int(a), '/', int(b))