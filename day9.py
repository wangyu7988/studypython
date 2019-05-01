class MyIterator:

    def __init__(self,x=2,xmax=100):
        self.__mul,self.__x = x,x
        self.__xmax = xmax

    def __iter__(self):
        return self

    def __next__(self):
        if self.__x and self.__x != 1:
            self.__mul *= self.__x
            if self.__mul <= self.__xmax:
                return self.__mul
            else:
                raise StopIteration
        else:
            raise StopIteration

if __name__ == '__main__':
    myiter = MyIterator()
    for i in myiter:
        print('迭代的数据元素为：',i)


class Counter:
    def __init__(self, x=0):
        self.x = x

counter = Counter()

def used_iter():
    counter.x += 1
    return counter.x


for i in iter(used_iter, 8):
    print('本次遍历的数值：', i)

import itertools
print(dir(itertools))

x= 0
for i in itertools.cycle('ab'):
    x += 1
    print(i)
    if x > 6:
        break

x= 0
for i in itertools.repeat('ab'):
    x += 1
    print(i)
    if x > 6:
        break


# 生成器

def myYield(n):

    while n>0:
        rcv = yield n
        n -= 1
        if rcv is not None:
          n = rcv

if __name__ == '__main__':
    for i in myYield(4):
        print("遍历得到的值：",i)
    print()
    my_yield = myYield(3)
    print('已经实例化生成器对象')
    print('test is',my_yield.__next__())
    print('第二次调用__next__()方法：')
    print('test is',my_yield.__next__())


    my_yield.send(10)
    print('test is',my_yield.__next__())
    print('test is',my_yield.__next__())


def consumer():
    print('等待接收处理任务...')
    while True:
        data = (yield)
        print('收到任务：', data)


def producer():
    c = consumer()
    c.__next__()
    for i in range(3):
        print('发送一个任务...', '任务%d' % i)
        c.send('第%d号任务' % i)
    c.send('hello')

if __name__ == '__main__':
    producer()

#装饰器
def abc(fun):
    def wrapper(*args, **kwargs):
        print('开始运行...')
        fun(*args, **kwargs)
        print('运行结束！')

    return wrapper


@abc
def demo_decoration(x,y):
    a = []
    b = []
    for i in range(x):
        a.append(i)
    for i in range(y):
        b.append(i)
    print(a)
    print(b)


@abc
def hello(name):
    print('Hello ', name)


if __name__ == '__main__':
    demo_decoration(5,6)
    print()
    hello('John')


def abc(myclass):
    class InnerClass:
        def __init__(self, z=0):
            self.z = z
            self.wrapper = myclass()

        def position(self):
            self.wrapper.position()
            print('z axis:', self.z)

    return InnerClass


@abc
class coordination:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def position(self):
        print('x axis:', self.x)
        print('y axis:', self.y)


if __name__ == '__main__':
    coor = coordination()
    coor.position()


