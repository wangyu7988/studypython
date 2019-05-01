import sqlite3
import random

src = 'abcdefghijklmnopqrstuvwxyz'
def get_str(x,y):
    str_sum = random.randint(x,y)
    astr = ''
    for i in range(str_sum):
        astr += random.choice(src)
    return astr

def output():
    cur.execute('select * from mytab')
    for sid,name,ps in cur:
        print(sid,' ',name,' ',ps)

def output_all():
    cur.execute('select * from mytab')
    for item in cur.fetchall():
        print(item)

def get_data_list(n):
    res = []
    for i in range(n):
        res.append((get_str(2,4),get_str(8,12)))
    return res
if __name__ == '__main__':
    print("建立连接...")
    con = sqlite3.connect(':memory:')
    print("建立游标...")
    cur = con.cursor()
    print('创建一张表mytab...')
    cur.execute('create table mytab(id integer primary key autoincrement not null,name text,passwd text)')
    print('插入一条记录...')
    cur.execute('insert into mytab (name,passwd)values(?,?)',(get_str(2,4),get_str(8,12),))
    print('显示所有记录...')
    output()
    print('批量插入多条记录...')
    cur.executemany('insert into mytab (name,passwd)values(?,?)',get_data_list(3))
    print("显示所有记录...")
    output_all()
    print('更新一条记录...')
    cur.execute('update mytab set name=? where id=?',('aaa',1))
    print('显示所有记录...')
    output()
    print('删除一条记录...')
    cur.execute('delete from  mytab where id=?',(3,))
    print('显示所有记录：')
    output()




from mysql import connector
import random

src = 'abcdefghijklmnopqrstuvwxyz'
def get_str(x,y):
    str_sum = random.randint(x,y)
    astr = ''
    for i in range(str_sum):
        astr += random.choice(src)
    return astr

def output():
    cur.execute('select * from mytab')
    for sid,name,ps in cur:
        print(sid,' ',name,' ',ps)

def output_all():
    cur.execute('select * from mytab')
    for item in cur.fetchall():
        print(item)

def get_data_list(n):
    res = []
    for i in range(n):
        res.append((get_str(2,4),get_str(8,12)))
    return res
if __name__ == '__main__':
    print("建立连接...")
    con = connector.connect(user='root',password='123456',database='test')
    print("建立游标...")
    cur = con.cursor()
    print('创建一张表mytab...')
    # cur.execute('create table mytab(id int primary key auto_increment not null,name text,passwd text)')
    print('插入一条记录...')
    cur.execute('insert into mytab (name,passwd)values(%s,%s)',(get_str(2,4),get_str(8,12),))
    print('显示所有记录...')
    output()
    print('批量插入多条记录...')
    cur.executemany('insert into mytab (name,passwd)values(%s,%s)',get_data_list(3))
    print("显示所有记录...")
    output_all()
    print('更新一条记录...')
    cur.execute('update mytab set name=%s where id=%s',('aaa',1))
    print('显示所有记录...')
    output()
    print('删除一条记录...')
    cur.execute('delete from  mytab where id=%s',(3,))
    print('显示所有记录：')
    output()



from pymongo import MongoClient
import random

src = 'abcdefghijklmnopqrstuvwxyz'
def get_str(x,y):
    str_sum = random.randint(x,y)
    astr = ''
    for i in range(str_sum):
        astr += random.choice(src)
    return astr

def get_data_list(n):
    res = []
    for i in range(n):
        res.append({'name':get_str(2,4),'passwd':get_str(8,12)})
    return res
if __name__ == '__main__':
    print("建立连接...")
    stus = MongoClient().test.stu
    print('插入一条记录...')
    stus.insert({'name':get_str(2,4),'passwd':get_str(8,12)})
    print("显示所有记录...")
    stu = stus.find_one()
    print(stu)
    print('批量插入多条记录...')
    stus.insert(get_data_list(3))
    print('显示所有记录...')
    for stu in stus.find():
        print(stu)
    print('更新一条记录...')
    name = input('请输入记录的name:')
    stus.update({'name':name},{'$set':{'name':'aaaa'}})
    print('显示所有记录...')
    for stu in stus.find():
        print(stu)
    print('删除一条记录...')
    name = input('请输入记录的name:')
    stus.remove({'name':name})
    print('显示所有记录...')
    for stu in stus.find():
        print(stu)

import random
from mongoengine import *

connect('test')


class Stu(Document):
    sid = SequenceField()
    name = StringField()
    passwd = StringField()

    def introduce(self):
        print('序号:', self.sid, end=" ")
        print('姓名:', self.name, end=' ')
        print('密码:', self.passwd)

    def set_pw(self, pw):
        if pw:
            self.passwd = pw
            self.save()


src = 'abcdefghijklmnopqrstuvwxyz'


def get_str(x, y):
    str_sum = random.randint(x, y)
    astr = ''
    for i in range(str_sum):
        astr += random.choice(src)
    return astr


if __name__ == '__main__':
    print('插入一个文档:')
    stu = Stu(name='lilei', passwd='123123')
    stu.save()

    stu = Stu.objects(name='lilei').first()

    if stu:
        stu.introduce()
    print('插入多个文档')
    for i in range(3):
        Stu(name=get_str(2, 4), passwd=get_str(6, 8)).save()

    stus = Stu.objects()
    for stu in stus:
        stu.introduce()

    print('修改一个文档')
    stu = Stu.objects(name='lilei').first()
    if stu:
        stu.name = 'aaaa'
        stu.save()
        stu.set_pw('bbbbbbbb')
        stu.introduce()

    print('删除一个文档')
    stu = Stu.objects(name='aaaa').first()
    stu.delete()

    stus = Stu.objects()
    for stu in stus:
        stu.introduce()





