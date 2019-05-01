class myclass:
     def info(self):
        print("this is the help")
     def plusab(self,x,y):
         print(x+y)

class demoinit:
    def __init__(self,x,y=0):
        self.x = x
        self.y = y
    def testplus(self):
        return self.x + self.y


dir(myclass)

myclass1 = myclass()

print(myclass1.__doc__)

help(myclass1)

myclass1.info()

myclass1.plusab(1,2)



demoinit1 = demoinit(3)
print(demoinit1.testplus())

demoinit2 = demoinit(3,7)
print(demoinit2.testplus())

#修改类变量和实例变量

class demo_property:
    class_name = 'demo'

    def __init__(self,x=0):
        self.x = x
    def class_info(self):
        print(demo_property.class_name)
        print(self.x)

    def change_property(self,name):
        demo_property.class_name = name  #这里不能用self

    def change_number(self,x):
        self.x = x


demo1 = demo_property()
demo2 = demo_property()

demo1.class_info()
demo2.class_info()

demo1.change_number(2)
demo2.change_number(3)
demo1.change_property('test')

demo1.class_info()
demo2.class_info()

#类的静态方法和类方法

class demomethod:
    def __init__(self,x=0):
        self.x = x

    @staticmethod
    def static_method():
        print('this is the static method')

    @classmethod
    def class_method(cls):
        print('this is the class method')


demomethod.static_method()
demomethod.class_method()

demo3 = demomethod()
demo3.static_method()
demo3.class_method()

#类的继承和重载


