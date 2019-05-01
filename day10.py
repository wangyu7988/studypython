class Duck:
    def __init__(self, name='duck'):
        self.name = name

    def quack(self):
        print("嘎嘎嘎...")


class Cat:
    def __init__(self, name='cat'):
        self.name = name

    def quack(self):
        print("喵喵喵...")


class Tree:
    def __init__(self, name='tree'):
        self.name = name


def duck_demo(obj):
    obj.quack()


if __name__ == '__main__':
    duck = Duck()
    cat = Cat()
    tree = Tree()
    duck_demo(duck)
    duck_demo(cat)
    try:
        duck_demo(tree)
    except AttributeError:
        print('atteributeerror')



import contextlib

@contextlib.contextmanager
def my_mgr(s,e):
    print(s)
    yield s + '  ' + e
    print(e)

if __name__ == '__main__':
    with my_mgr('start','end') as val:
        print(val)


class DemoClass:
    class_val = 3

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.info()

    def info(self):
        print('类属性class_val：', DemoClass.class_val)
        print('实例属性x：', self.x)
        print('实例属性y：', self.y)


if __name__ == '__main__':
    dc = DemoClass()
    if hasattr(DemoClass, 'class_val'):
        setattr(DemoClass, 'class_val', 1000)
    if hasattr(dc, 'x'):
        setattr(dc, 'x', 'xxxxxxxx')
    if hasattr(dc, 'y'):
        setattr(dc, 'y', 'yyyyyyyy')
    dc.info()
    setattr(dc, 'z', 'zzzzzzzz')
    print('添加的属性z', dc.z)


class Book:

    def __init__(self, name="Python 从入门到精通"):
        self.name = name

    def __add__(self, obj):
        return self.name + ' add ' + obj.name

    def __len__(self):
        return len(self.name)


if __name__ == '__main__':
    booka = Book()
    bookb = Book('Java 从入门到精通')
    print("len(booka):", len(booka))
    print('len(bookb):', len(bookb))
    print(booka + bookb)

