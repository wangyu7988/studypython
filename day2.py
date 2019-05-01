
import math
import boto3
#计算2的平方根
print(math.sqrt(2))

#python里面浮点数相加跟实际看到的结果不一定一致
print(0.1+0.1+0.1)

#判断两个浮点数是不是相等用这两个浮点数相减之后与10的负10次方相比，如果比10的负10次方相比小，就认为相等
print(0.1+0.1+0.1-0.3 < 10**-10)

#判断是不是质数
def is_prime(i):
    for j in range(2,i-1):
        if i % j ==0:
            return True

    return False

#number=input("please input your name:")
number="wangyu"
print("your name is",number)

print(number,3, sep=",")
print(number,3,end='.');print(3,number)


x=4
y=2*x-8+x/2
print(y)

# 取绝对值
print(abs(-4))



'''for i in range(10):
    print("the number is:")
    print(i)
    if is_prime(i):
        print(i)
    else:
      print(0)
'''

