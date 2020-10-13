#方法1
#分解质因数
#去掉相同的质因数

a = int(input('请输入分子：'))
b = int(input('请输入分母：'))


def prime_factor(c):
    p = []
    for i in primes:
        while c % i == 0:
            p.append(i)
            c /= i
    return p


def get_primes(c):
    p = []
    flag = 0
    for i in range(2, c + 1):
        for j in range(2, i):
           if i % j == 0:
               flag = 1
               break

        if flag == 0:
            p.append(i)
        else:
            flag = 0

    return p


primes = []
primes_a = []
primes_b = []

if abs(a) > abs(b):
    primes = get_primes(a)
else:
    primes = get_primes(b)
primes_a = prime_factor(a)
primes_b = prime_factor(b)

for i in primes_a:
    if i in primes_b:
        a /= i
        b /= i
print(int(a), '/', int(b))
