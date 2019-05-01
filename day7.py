def testTryAll(index,i):
    stulst = ["John","Jenny","Tom"]
    try:
        print(len(stulst[index])/i)
    except (IndexError,ZeroDivisionError) :
        print("Error!")

print('Try all...Right')
testTryAll(1,2)
print('Try all...one Error')
testTryAll(1,0)
print('Try all...two Error')
testTryAll(4,0)

class RangeError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
      return self.value

    errorinfo = "customer error"


def testRaise():
    for i in range(5):
        try:
            if i==2:
                raise RangeError("test")
        except RangeError:
            print(RangeError("test").value)
        finally:
            print(i)
    print('end...')

testRaise()




#error1 = RangeError('class error')
# raise RangeError('Range Error!')


def grade(sum):
    """
    >>> grade(100)
    '优秀'
    >>> grade(80)
    '良'
    >>> grade(65)
    '合格'
    >>> grade(10)
    '不合格'
    """
    if sum > 90:
        return '优秀'
    if sum > 80:
        return '良'
    if sum > 60:
        return '合格'
    if sum < 60:
        return '不合格'

if __name__ == '__main__':
    import doctest
    doctest.testmod()



import pdb

def sum(maxint):
    s = 0
    for i in range(maxint):
        s += i
    print(s)
    return s

pdb.runcall(sum,10)

pdb.run("""
for i in range(3):
    print(i)
""")
