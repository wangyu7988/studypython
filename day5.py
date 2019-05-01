def helloworld():
    print("hello world!")

def testplus(number):
    result = 0
    for i in range(int(number)):
        result += i
    return result

def testplus2(number):
    result = 0
    for i in number:
        result += i
    return result

def testplus3(a,b):
    global x  #函数内的变量如果想改变作用于需要用关键字global 声明
    x = a+b
    print(x)

#默认参数函数
def testpara1(firstname='wang',givenname='yu'):
    print('your name is %s %s' % (firstname,givenname))  #注意多个参数要括起来

#可变参数调用 一个星代表未知参数 两个星代表收集关键字信息的可变参数

def testpara2(*para):
    print(type(para))
    print(para)

def testpara3(a,b=1,**dict):
    print(dict)
    print(a+b)


helloworld()

print(testplus(5.2))

print(testplus2([2.0,3**2,6e3]))

testpara1()
testpara1('ren','lili')

testpara2(1,2,3)
testpara2('wang')

testpara3(0,k='wang',j='yu')


#调用多个参数的函数的时候，可以用一个星号或者2个星号来拆解参数

testplus3(*(3,4))
testplus3(**{'a':3,'b':4})

print(x)


#定义匿名函数用lambda关键字

sum = lambda i,j:i+j
print(sum(3,4))
