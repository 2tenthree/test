from functools import reduce


def normalize(name):
    y = name.lower()
    y = name.title()
    return y


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    def qiuji(x,y):
        return x * y
    return reduce(qiuji,L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def str2float(s):
    dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    pointp = s.index('.')

    def qiuzheng(z,i):
        return z * 10 + i

    def qiuxiaoshu(f,l):
        return 0.1 * f + l
    strlis = s.split('.')

    def bianzheng(ss):
        return dic[ss]

    zhengshuz = reduce(qiuzheng,map(bianzheng,strlis[0]))
    xiaoshuz = reduce(qiuxiaoshu,map(bianzheng, strlis[1][::-1]))
    return zhengshuz + xiaoshuz *0.1


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
