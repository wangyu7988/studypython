#字符串
string1="ab"

#反斜杠转义输出
string2="ab\"c\""

print(string1)
print(string2)

#\t是制表符 \n是回车  \\是输出反斜杠
print('ab\tab\nt\\c')

#字符串*4表示输出4遍
print(string1*4)

#求字符串长度
print(len(string1))

#find找字符串，找不到返回-1
print('abdasdjasdasd'.find('da'))

#join是以逗号分隔字符串
print(','.join('abdasdasd'))

#split是以逗号分字符串为列表
print('a,b,s,d,c,a,s,d,a'.split(','))

print(23)
print(0b1011) #二进制写法
print(0x10)   #16进制写法
print(0o12)   #八进制写法 第二个是字母o

print(2**3)  #2的3次方
print(5//4)  #整除法
print(6%4)   #取余

#浮点数写法
19.
.98
-2e3  #-2 乘以10的3次方

#类型转换

int(2.1)  #转换为整数

int('23')

str(23.4)  #将浮点数转换为字符串

float('233.3')  #将字符串转换为浮点数

int('2a',base=16) #将16进制字符串转换为整数

#  int(input())  input默认为字符串

r'abdsad\.'  #字符串前面加r表示转义字符串 斜杠不需要用两个\\

print('%d + %d = %f' % (2,3,5))   #格式化字符串， %表示替换标志符

string3='我爱python'
string4=string3.encode('utf-8')   #encode是转换为字符编码
string5=string4.decode('utf-8')   #decode是从字符编码转换为字符
print(string4,string5)

print(string3.encode('gbk').decode('gbk'))    #转换为gbk字符编码

list()  #初始化列表

[123,'str',123.123]  #列表赋值

[123.123,123] + [123,322]   #列表加法

print([1,] * 4)  #列表乘法，就是四个1

list1 = [1,2]
list1.append(3)
list1.extend([1,2]) #追加另一个列表
list1.pop()  #删除列表最后一个内容
list1.sort()

tuple()  #创建元组

(1,2,'323',2.11)   #元组是小括号，元组当中的数据不能修改，但是列表可以

print(list1.count(1)) #查询列表中出现1的次数
print(list1[3])  #访问列表第三个元素，从0开始，第三个元素就是0.1.2
print(list1)

x=3
y=3
x is y

1<x<3

1 in (1,2)

#字典，相当于key value
dict1={'a':1, 'b':2}
dict1.items()
dict1.keys()
dict1.get('a')
dict1['a']

print(dict1['a'])

#序列  相当于操作列表

list1[0:2]

sum(list1) #对序列当中所有元素求和

any(list1)

all(list1)
list1[-1]


print('please input your name:')
yourname=input()


#--------------这么长一段跟下面一句话一个意思
your_new_name =  yourname.split()
print(your_new_name)

print(len(your_new_name))

for i in range(len(your_new_name)):
    print(your_new_name[i].capitalize(),end=' ')

print('\n')

#-----------就是这句话-----fuck
print('your name is %s' % yourname.title())






