# -*- coding:utf-8 -*-
#
import re
import sys
import os

s="how are you"
re.match("how",s)
re.search("how",s)
re.findall("how",s)

re.match("h.*",s,re.I)
re.findall('[a-z]{3}',s) #匹配三个字符

re.findall('[a-z]{1,3}',s)  #匹配最小1个字符，最大3个字符

re.sub("how","when",s)  #将how 替换为when

re.subn("how","when",s)   #返回替换次数
re.split(" ",s) #以空格分隔

cellnumber = "Phone:+86-18611648790"
res = re.compile(r'(\d+)-(\d+)')

number = res.search(cellnumber)

number.group(1)
number.group(2)
number.groups()

r = re.compile(r'are(?=\syou)')

r.search(s)


def DealWithFunc(s):
	r = re.compile(r'''
		(?<=def\s)
		\w+
		\(.*?\)
		(?=:)
		''',re.X | re.U)
	return r.findall(s)
def DealWithVar(s):
	vars = []
	r = re.compile(r'''
		\b
		\w+
		(?=\s=)
		''',re.X | re.U)
	vars.extend(r.findall(s))
	r = re.compile(r'''
		(?<=for\s)
		\w+
		\s
		(?=in)
		''',re.X | re.U)
	vars.extend(r.findall(s))
	return vars


filelists = os.listdir(os.getcwd())

pyfiles = []
for files in filelists:
     if re.findall("py$",files):
        #pyfiles.append(files)
       # print(re.findall("py$",files))
        file = open(files, encoding="utf-8")
        s = file.readlines()
        file.close()
        print('********************************')
        print(files, '中的函数有：')
        print('********************************')
        i = 0
        for line in s:
            i = i + 1
            function = DealWithFunc(line)
            if len(function) == 1:
                print('Line: ', i, '\t', function[0])
        print('********************************')
        print(files, '中的变量有：')
        print('********************************')
        i = 0
        for line in s:
            i = i + 1
            var = DealWithVar(line)
            if len(var) == 1:
                print('Line: ', i, '\t', var[0])

pyfiles.sort()
print(pyfiles)

'''if len(sys.argv) == 1:
	sour = input('请输入要处理的文件路径：')
else:
	sour = sys.argv[1]



file = open(sour,encoding="utf-8")
s = file.readlines()
file.close()
print('********************************')
print(sour,'中的函数有：')
print('********************************')
i = 0
for line in s:
	i = i + 1
	function = DealWithFunc(line)
	if len(function) == 1:
		print('Line: ',i,'\t',function[0])
print('********************************')
print(sour,'中的变量有：')
print('********************************')
i = 0
for line in s:
	i = i + 1
	var = DealWithVar(line)
	if len(var) == 1:
		print('Line: ',i,'\t',var[0])
'''