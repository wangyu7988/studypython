import threading
def thrfun(x,y):
    for i in range(x,y):
        print(str(i*i)+';')
ta = threading.Thread(target=thrfun,args=(1,6))
tb = threading.Thread(target=thrfun,args=(16,21))
ta.start()
tb.start()


class myThread(threading.Thread):
    def __init__(self,mynum):
        super().__init__()
        self.mynum = mynum

    def run(self):
        for i in range(self.mynum,self.mynum+5):
            print(str(i*i)+';')

ma = myThread(1)
mb = myThread(16)
ma.start()  # start方法是mythread类的启动方法
mb.start()


import time
def thrfun(x,y,thr=None):

    if thr:
        thr.join()  #这句话的意思是等待当前线程方法运行完之后才可以运行第二个
    else:
        time.sleep(2)
    for i in range(x,y):
        print(str(i*i)+';')
ta = threading.Thread(target=thrfun,args=(1,6))

print("test")
tb = threading.Thread(target=thrfun,args=(16,21,ta))
ta.start()
tb.start()


class myThread(threading.Thread):
    def __init__(self,mynum):
        super().__init__()
        self.mynum = mynum

    def run(self):
        time.sleep(1)
        for i in range(self.mynum,self.mynum+5):
            print(str(i*i)+';')

def main():
    print('start...')
    ma = myThread(1)
    mb = myThread(16)
    ma.daemon = True
    mb.daemon = True   #daemon是在后台运行的，前台看不到输出
    ma.start()
    mb.start()
    print('end...')
if __name__ == "__main__":
    main()


class myThread(threading.Thread):
    def run(self):
        global x
        lock.acquire()
        for i in range(3):
            x += 10
        time.sleep(1)
        print(x)
        lock.release()  #加锁的意思是防止多个线程同时对x进行访问
x = 0
lock = threading.RLock()
def main():
    thrs = []
    for item in range(5):
        thrs.append(myThread())
    for item in thrs:
        item.start()
if __name__ == "__main__":
    main()

for i in range(3):
    print(i)


class myThreada(threading.Thread):
    def run(self):
        evt.wait()
        print(self.name, ':Good morning!')
        evt.clear()
        time.sleep(1)
        evt.set()
        time.sleep(1)
        evt.wait()
        print(self.name, ":I'm fine,thank you.")


class myThreadb(threading.Thread):
    def run(self):
        print(self.name, ':Good morning!')
        evt.set()
        time.sleep(1)
        evt.wait()
        print(self.name, ':How are you?')
        evt.clear()
        time.sleep(1)
        evt.set()


evt = threading.Event()


def main():
    John = myThreada()
    John.name = "John"
    Smith = myThreadb()
    Smith.name = 'Smith'
    John.start()
    Smith.start()


if __name__ == "__main__":
    main()


import subprocess
print('call() test:',subprocess.call(['python','protest.py']))
print('')
print('check_call() test:',subprocess.check_call(['python','protest.py']))
print('')
print('getstatusoutput() test:',subprocess.getstatusoutput(['python','protest.py']))
print('')
print('getoutput() test:',subprocess.getoutput(['python','protest.py']))
print('')
print('check_output() test:',subprocess.check_output(['python','protest.py']))


#communicate0是标准子进程标准输出，1是标准错误输出

import subprocess
prcs = subprocess.Popen(['python','protest.py'],
                        stdout=subprocess.PIPE,
                        stdin=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True,
                        shell=True)
prcs.communicate('These strings are from stdin.')
print("subprocess pid:",prcs.pid)
print('\nSTDOUT:')
print(str(prcs.communicate()[0]))
print('STDERR:')
print(prcs.communicate()[1])



import subprocess
processes = []
psum = 5
for i in range(psum):
    processes.append(subprocess.Popen(['python','protest9.py'],
                        stdout=subprocess.PIPE,
                        stdin=subprocess.PIPE,
                        universal_newlines=True,
                        shell=True))

processes[0].communicate('0 bouquet of flowers!')
for before,after in zip(processes[:psum],processes[1:]):
    after.communicate(before.communicate()[0])
print('\nSum of Processes :%d' % psum)
print()
for item in processes:
    print(item.communicate()[0])
    print(item.communicate()[1])

