def file_hdl(name='test.txt'):
    f = open(name)
    res = 0
    i = 0
    for line in f:
#       i += 1
        print('第%s行的数据为：' % line.strip(),line)
        res += int(line)

    print('这些数的和为：',res)
    print(f.name)
    f.close()
if __name__ == '__main__':
    file_hdl()


import fileinput
def demo_fileinput():
    with fileinput.input(['test.txt']) as lines:
        for line in lines:
            print("总第%d行," % lines.lineno(),
                  "文件%s中第%d行：" %
                  (fileinput.filename(),fileinput.filelineno()))
            print(line.strip())

if __name__ == '__main__':
    demo_fileinput()

import os

filenames = []

for a,b, files in os.walk('test'): #遍历test文件夹下的所有文件, a,b是固定写法，参考手册
    print(a)
    print(b)
    print(files)
    if files:
        filenames.append([file[:-4] for file in files])  #去掉后缀名，相当于从最后一个文件名字符向左数4个

for name1 in filenames:
    print(name1)

fname = 'testexam'
i = 0

for files in filenames:
        f = open(fname + str(i) + '.xls', 'w')           #w表示文件可写，没有这个文件则创建文件
        for name in files:
            print(name)
            f.write(name[-2:] + '\t' + name[:-2] + '\n')   #冒号在右表示从最右的第2个字符到最右端，冒号在左表示从最左端到右侧第二个字符出
        f.close()
        i += 1


#from distutils.core import setup
#import py2exe

#setup(console=['day7.py'])

import os
perfix = 'Python'
length = 2
base = 1
format = 'mdb'
def PadLeft(str , num , padstr):
    stringlength = len (str)
    n = num - stringlength
    if n >=0 :
        str=padstr * n + str
    return str

print('the files in %s will be renamed' % os.getcwd())
all_files = os.listdir(os.getcwd())
print([f for f in all_files if os.path.isfile(f)])
input = input('press y to continue\n')
if input.lower() != 'y':	exit()
filenames = os.listdir(os.curdir)
i = base - 1
for filename in filenames:
    i = i+1
    if filename != "rename.py" and os.path.isfile(filename):
        name = str(i)
        name = PadLeft(name,length,'0')
        t = filename.split('.')
        m = len(t)
        if format == '':
            os.rename(filename,perfix+name+'.'+t[m-1])
        else:
            if t[m-1] == format:
                os.rename(filename,perfix+name+'.'+t[m-1])
            else:
                i = i - 1
    else:
        i = i - 1
all_files = os.listdir(os.getcwd())
print([f for f in all_files if os.path.isfile(f)])


