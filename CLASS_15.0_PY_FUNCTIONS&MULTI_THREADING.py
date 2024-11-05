##class 15-----Multi threading






##def fun():
##    print("success")
##    print(time.ctime())
##    time.sleep(2)
##def fun1():
##    print('good')
##    print(time.ctime())
##fun()
##fun1()
##output::
##success
##Traceback (most recent call last):
##  File "D:\NAL_STUDY_MATERIAL\BPY_MATERIAL\BPY_NOTES\CLASS_15_PY_FUNCTIONS.py", line 9, in <module>
##    fun()
##  File "D:\NAL_STUDY_MATERIAL\BPY_MATERIAL\BPY_NOTES\CLASS_15_PY_FUNCTIONS.py", line 4, in fun
##    print(time.ctime())
##NameError: name 'time' is not defined

##introduction to libraries::
import time
def fun():
    print("success")
    time.sleep(2)##2 implifies the delay time 2 second
    print(time.ctime())
  
def fun1():
    print('good')
    print(time.ctime())
fun()
fun1()


#####output:
##    success
##Fri May  6 07:25:32 2022
##good
##Fri May  6 07:25:34 2022
print("nxt prg----------------------2")
##without 2 sleep
import time
def fun():
    print("success")
    print(time.ctime())
    
def fun1():
    print('good')
    print(time.ctime())
fun()
fun1()
##output::
##    success
##Fri May  6 07:45:28 2022
##good
##Fri May  6 07:45:28 2022
##successgood
print("nxt prg----------------------3")
## running without delay..............same time output
import time
import threading
def fun():
    print("success")
    
    print(time.ctime())
    
def fun1():
    print('good')
    print(time.ctime())
t1=threading.Thread(target=fun)
t2=threading.Thread(target=fun1)
t1.start()
t2.start()
##output::
##successgood
##
##
##Fri May  6 07:41:21 2022Fri May  6 07:41:21 2022
##
##running simultaneously...........side by side...............fun:fun1

print("nxt prg----------------------4")


##1......passing arguements in threading function
##2...... delaying in threading


##1) arguements::
##import time
##import threading
##def fun(name):
##    print(name,time.ctime())
##def fun1():
##    print(name,time.ctime())
##t1=threading.Thread(target=fun,args=('dhoni'))
##t2=threading.Thread(target=fun1,args=('mccullum'))
##t1.start()
##t2.start()
##
##output:::TypeErrorTypeError: : fun() takes 1 positional argument but 5 were givenfun1() takes 0 positional arguments but 8 were given


print("nxt prg----------------------5")

import time
import threading
def fun(name):
    print(name,time.ctime())
def fun1(name):
    print(name,time.ctime())
t1=threading.Thread(target=fun,args=('dhoni',))
t2=threading.Thread(target=fun1,args=('mccullum',))
t1.start()
t2.start()



##output::::
##dhonimccullum
##  Fri May  6 08:04:16 2022Fri May  6 08:04:16 2022
##

