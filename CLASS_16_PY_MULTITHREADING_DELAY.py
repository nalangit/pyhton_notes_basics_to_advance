###_____________________________________may 8-------------------------------
### how to make delay in threading






##import threading
##import time
##def fun(name,delay):
##    count=0
##    while(count<5):
##        print(name,time.ctime())
##        count=count+1
##        time.sleep(delay)
##t1=threading.Thread(target=fun,args=('dhoni',2))
##t2=threading.Thread(target=fun,args=('kholi',4))
##t1.start()
##t2.start()



##output;;

##
##dhonikholi  Mon May  9 07:31:33 2022Mon May  9 07:31:33 2022
##
##dhoni Mon May  9 07:31:35 2022
##kholi Mon May  9 07:31:37 2022
##dhoni Mon May  9 07:31:37 2022
##dhoni Mon May  9 07:31:39 2022
##kholi Mon May  9 07:31:41 2022
##dhoni Mon May  9 07:31:41 2022
##kholi Mon May  9 07:31:45 2022
##kholi Mon May  9 07:31:49 2022
##
##
##
##import threading
##import time
##def fun(name):
##    new()
##    print(name,x)
##x=0
##def new():
##    global x
##    x=x+1
##t1=threading.Thread(target=fun,args=('dhoni',))
##t2=threading.Thread(target=fun,args=('kholi',))
##t1.start()
##t2.start()


##global interpreter LOCK(GIL):::
##.Lock()
#.acquire()
#.release()

print('nxt-------prg')


import threading
import time
def fun(name,L):
 L.acquire()
 new()
 print(name,x)
 L.release()


x=0

def new():
    global x
    x=x+1


L=threading.Lock()
t1=threading.Thread(target=fun,args=('dhoni',L))
t2=threading.Thread(target=fun,args=('kholi',L))
t1.start()
t2.start()

#.lock() which dosent allows the program to run the nxt statement until the previous one gets 
