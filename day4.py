import math

def output_key_value(dict):
    for key, value in dict.items():
        print(key, ':', value)


x=input('please input a number:\n')
x=int(x)
if x < 0:
    print('the number < 0')
    x = -x
elif x==0:
    print('the number is zero')
else:
    print('the number > 0')


for i in range(0,x,2):
    print(i)
    if i == 4:
        break

dict1={'a':1,'b':2,'c':3}
for key,value in dict1.items():
    print(key,':',value)

list1 = [1,2,3,4]
list2 = [2*i for i in list1]
list3 = ['a','b','c','d']

for i in range(len(list2)):
    print(list2[i])

dict2={ k:v for k,v in zip(list3,list1)}  #合并两个列表，组成key value

output_key_value(dict2)









