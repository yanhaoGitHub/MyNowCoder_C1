import random
import re
def demo_string():
    stra = "hello world"
    print stra.upper();
    print stra.replace("world","nowcoder")
    #the end \ flag is mean let the next line follow this line,do not 2 line.
    print "aaaaaaaaaaaaaa"\
    "bbbbbbbbbbbbb"

    strb = "\n\n\nthis is my python code\n\t"
    print 1, strb.lstrip()
    print 2, strb.rstrip()

    strc = "abc"
    print 3, len(strc)

    print 4, "-".join(['aa','bb','cc'])

    strd = "abc def"
    print 5, strd.split(" ")

def demo_operation():
    print 1,":",1+2, 5/2, 3*4, 10%3
    print 2,":",True, not True
    print 3, ":", 2<<3, 2<<1
    print 4, ":", 5|3, 5&3, 5^3
    x = 1
    y = 3.3
    print x, y, type(x), type(y)

def demo_buildinfunction():
    print 1, max(2,5), min(6,9)
    print 2, len("xxx"), len([1,2,3,4])
    print 3, abs(-2) #jueduizhi
    print 4, range(1,10,3) #(start, stop, step)
    print 5, dir(list)
    x = 2
    print 6,eval("x + 6")
    print 7, chr(97), ord('a')
    print 8, divmod(11, 3)  #11/3 = 3  yu 2

def demo_controlFlow():
    #if language
    score = 65
    if score>99:
        print 1,"A"
    elif score > 60:
        print 2, 'B'
    else:
        print 3, 'C'

    #while language
    while (score < 100):
        print score
        score+=10
    #for language
    #continue, break, pass
    for i in range(0, 10):
        if i == 0:
            pass  #do_special
            #print 3, i
        if i < 5:
            continue
        if i == 7:
            break
        print 3, i

def demo_list():
    lista = [1,2,3,4,5] #ArrayList
    print 1, lista
    listb = ['aa', 1, 'bb', 1.1]
    print 2, listb
    lista.extend(listb)    #lista add listb
    print 3, lista
    print 4, len(lista) #9
    print 5, 'aa' in lista  #true
    listb.insert(0, 'www')
    print 6, listb   #add 'www' in listb' index 0
    #listb.pop(1) #pop index 1 of listb
    #print 7, listb
    listb.reverse()  #reverse listb
    print 8, listb
    print 9, listb[0], listb[1]
    listb.sort()   #sort
    print 10, listb
    listb.sort(reverse=True)
    print 11, listb
    print 12, listb * 2
    print 13, [0] * 12
    tuplea = (1,2,3)
    listaa = [1,2,3]  #can not append
    listaa.append(4)  #can append
    print 14, listaa

def demo_dict():
    dicta = {4:16, 1:1, 2:4, 3:9}   # hashMap hashTable
    print 1, dicta
    print 2, dicta.keys()
    print 3, dicta.values()
    print 4, dicta.has_key(2), dicta.has_key(9)  #true, false
    # for map<> iterator
    for key, value in dicta.items():
        print 'key-value:', key, value

    dictb = {"+":add, "-":sub}
    print 5, dictb["+"](1,2)
    print 6, dictb["-"](19,6)
    print 7, dictb.get("-")(15,3)
    dictb['*'] = 'X'
    print 8, dictb
    dicta.pop(4)
    print dicta
    del dicta[1]
    print dicta


def add(a, b):
    return a + b
def sub(a, b):
    return a - b

def demo_set():
    seta = set((1,2,3))
    print 1, seta
    setb = set((2,3,4))
    print 2, setb
    print 3, seta.intersection(setb)   #jiao
    print 4, seta & setb   #jiao
    print 5, seta | setb #bing
    print 6, seta.union(setb)   #bing
    print 7, seta - setb
    seta.add("x")
    print seta
    print 8, len(seta)

#OOP  Origin__Object__Demo

def demo_random():
    #random.seed(1)
    #x = prex  * 1000007 % 100023
    print 1, random.random()
    print 2, random.random() * 100
    print 3, int(random.random() * 100)
    print 4, random.randint(0, 200)
    print 5, random.choice(range(0, 100))   #select one number from 0 to 100
    print 6, random.sample(range(0, 100), 4)  #select 4 number from 0 to 100

    a = [1,2,3,4,5]
    random.shuffle(a)  #suiji daluan
    print 7, a

def demo_re():
    str = "abc123def12gh15"
    # + one or more
    # * 0 or more
    # ? 0 or one
    p1 = re.compile('[\d]+')    # find numbers
    p2 = re.compile('[\d]')
    print 1, p1.findall(str)   # ['123', '12', '15']
    print 2, p2.findall(str)   #['1', '2', '3', '1', '2', '1', '5']

    strb = 'a@163.com;b@gmail.com;c@qq.com'
    # w 0~9 a~z A~Z
    p3 = re.compile('[\w]+@[163|qq]+\.com')
    print 3, p3.findall(strb)   #['a@163.com', 'c@qq.com']

    strc = "<html><h>title</h><body>xxx</body></html>"
    p4 = re.compile('<h>[^<]+</h>')
    print 4, p4.findall(strc)   # ['<h>title</h>']
    p5 = re.compile('<h>([^<]+)</h>')
    print 5, p5.findall(strc)   # ['title']

    strd = "xxx2016-06-29ccaca"
    p6 = re.compile('\d\d\d\d-\d\d-\d\d')
    print 6, p6.findall(strd)    #['2016-06-29']
    p7 = re.compile('\d{4}-\d{2}-\d{2}')
    print 7, p7.findall(strd)    #['2016-06-29']




#main method
if __name__ == "__main__":
    #demo_string()
    #demo_operation()
    #demo_buildinfunction()
    #demo_controlFlow()
    #demo_list()
    #demo_dict()
    #demo_set()
    #demo_random()
    demo_re()