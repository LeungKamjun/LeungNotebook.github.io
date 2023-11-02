# 变量
num = 100
name = 'calulate'


# 函数
def add(*args):
    if len(args) > 1:
        sum = 0
        for i in args:
            sum += i
        return sum
    else:
        print('至少传入两个参数')


def minus(*args):
    if len(args) > 1:
        m = 0
        for i in args:
            m -= i
        return m
    else:
        print('至少传入两个参数')


# 类
class Calulate:
    def __init__(self, num):
        self.num = num

    def test(self):
        print('正在使用Calulate进行运算')

    @classmethod
    def test1(cls):
        print('正在调用Calulate中的类方法')
