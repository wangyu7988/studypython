'''import socket

HOST = ''
PORT = 10888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Client\'s Address:', addr)
while True:
    data = conn.recv(1024)
    print("Receive Data:",data.decode('utf-8'))
    if not data:
        break
    conn.sendall(data)
conn.close()


import socket

HOST = 'localhost'
PORT = 10888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = "你好！"
while data:
    s.sendall(data.encode('utf-8'))
    data = s.recv(512)
    print("Receive from server:\n",data.decode('utf-8'))
    data = input('please input a info:\n')
s.close()
'''
from http.client import HTTPConnection

mc = HTTPConnection('www.baidu.com:80')
mc.request('GET','/')
res = mc.getresponse()
print(res.status,res.reason)
print(res.read().decode('utf-8'))



from urllib.request import urlopen

from urllib.parse import urlencode
import re

##wd = input('输入一个要搜索的关键字：')
wd= 'python'
wd = urlencode({'wd':wd})
url = 'http://www.baidu.com/s?' + wd
page = urlopen(url).read()
content = (page.decode('utf-8')).replace("\n","").replace("\t","")
title = re.findall(r'<h3 class="t".*?h3>', content)
title = [item[item.find('href =')+6:item.find('target=')] for item in title]
title = [item.replace(' ','').replace('"','') for item in title]
for item in title:
    print(item)



from poplib import POP3
import re,email,email.header
#from p_email import mypass

def decode_email_content(msg_src,names):
    msg = email.message_from_bytes(msg_src)
    result = {}
    for name in names:
        content = msg.get(name)
        info = email.header.decode_header(content)
        if info[0][1]:
            if info[0][1].find('unknown-') == -1:
                result[name] = info[0][0].decode(info[0][1])
            else:
                try:
                    result[name] = info[0][0].decode('gbk')
                except:
                    result[name] = info[0][0].decode('utf-8')
        else:
            result[name] = info[0][0]
    return result

if __name__ == "__main__":
    pp = POP3("pop3.163.com")
    pp.user('wangyu7988@163.com')
    pp.pass_('wang0709')
    total,totalnum = pp.stat()
    print(total,totalnum)

    for i in range(total-10,total):
        hinfo,msgs,octet = pp.top(i+1,0)
        b=b''
        for msg in msgs:
            b += msg+b'\n'
        items = decode_email_content(b,['subject','from'])
        print(items['subject'],'\nFrom:',items['from'])
        print()
    pp.close()



import smtplib,email

chst = email.charset.Charset(input_charset='utf-8')
header = ("From: %s\nTo: %s\nSubject: %s\n\n"
       % ("wangyu7988@163.com",
          "wangyu7988@163.com" ,
          chst.header_encode("Python smtplib 测试！")))
body = "你好！"
email_con = header.encode('utf-8') + body.encode('utf-8')
smtp = smtplib.SMTP("smtp.163.com")
smtp.login("wangyu7988@163.com",'wang0709')
smtp.sendmail("wangyu7988@163.com","wangyu7988@163.com",email_con)
smtp.quit()

# -*- coding:utf-8 -*-
#
from ftplib import FTP
bufsize = 1024
def Get(filename):
    command = 'RETR ' + filename
    ftp.retrbinary(command, open(filename,'wb').write, bufsize)
    print('下载成功')
def Put(filename):
    command = 'STOR ' + filename
    filehandler = open(filename,'rb')
    ftp.storbinary(command,filehandler,bufsize)
    filehandler.close()
    print('上传成功')
def PWD():
    print(ftp.pwd())
def Size(filename):
    print(ftp.size(filename))
def Help():
    print('''   
    ==================================
        Simple Python FTP 
    ==================================
    cd        进入文件夹
    delete        删除文件
    dir        获取当前文件列表
    get        下载文件
    help        帮助
    mkdir        创建文件夹
    put        上传文件
    pwd        获取当前目录
    rename        重命名文件
    rmdir        删除文件夹
    size        获取文件大小
    ''')
server = input('请输入FTP服务器地址:')
ftp = FTP(server)
username = input('请输入用户名:')
password = input('请输入密码:')
ftp.login(username,password)
print(ftp.getwelcome())
actions  = {'dir':ftp.dir, 'pwd': PWD, 'cd':ftp.cwd, 'get':Get,
        'put':Put, 'help':Help, 'rmdir': ftp.rmd, 
        'mkdir': ftp.mkd, 'delete':ftp.delete,
        'size':Size, 'rename':ftp.rename}
while True:
    print('pyftp>')
    cmds = input()
    cmd = str.split(cmds)
    try:
        if len(cmd) == 1:
            if str.lower(cmd[0]) == 'quit':
                break
            else:
                actions[str.lower(cmd[0])]()
        elif len(cmd) == 2:
            actions[str.lower(cmd[0])](cmd[1])
        elif len(cmd) == 3:
            actions[str.lower(cmd[0])](cmd[1],cmd[2])
        else:
            print('输入错误')
    except:
        print('命令出错')
ftp.quit()
    
