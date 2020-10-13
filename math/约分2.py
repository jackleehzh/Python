#方法2
#同时除以最大公约数

#辗转相除法
def gcd(a, b):
    while a % b != 0:
        c = a % b
        a = b
        b = c

    return b


a = int(input('请输入分子：'))
b = int(input('请输入分母：'))

c = gcd(a, b)

print(int(a / c), '/', int(b / c))
