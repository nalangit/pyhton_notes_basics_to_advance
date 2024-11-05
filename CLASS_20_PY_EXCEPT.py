#CLASS_20  # error & exception
try:
     var =10
     if(var>5):
         raise Error
except:
    print("good")

#it will print "good "in output  because the condition is satisfied and error is raised ,
    #
    

    
print('nxt prg------------2')



try:
     var =10
     if(var>5):
         raise TypeError
except:
    print("good")

print('nxt prg------------3')

##try:
##     var =10
##     if(var>5):
##         raise Error("bad")
##except Error as a:
##    print(a)

try:
     var =10
     if(var>5):
         raise TypeError("bad")
except TypeError as a:
    print(a)


print('nxt prg------------4')

try:
     var =10
     if(var>5):
         raise Exception("bad")
except Exception as a:
    print(a)
print('nxt prg------------5')


##CLASS:::
class Error(Exception):
    var="bad"

try:
     var =10
     if(var>5):
         raise Error("bad")
except Error as a:
    print(a.var)



var=10/0
print(var)
---------------------------------------------------------------------------
ZeroDivisionError Traceback (most recent call last)
<ipython-input-1-0322b256df35> in <module> ----> 1 var=10/0 2 print(var)
ZeroDivisionError: division by zero
[2]
try:
    var=10/0
    print(var)
except:
    print("bad")
bad

[7]
try:
    ##var="str"+10
    ##var=10/0
    var=dhoni
    print(var)
except(ZeroDivisionError):
    print("bad")
    
---------------------------------------------------------------------------
NameError Traceback (most recent call last)
<ipython-input-7-b2e9d073dbed> in <module> 2 ##var="str"+10 3 ##var=10/0 ----> 4 var=dhoni 5 print(var) 6 except(ZeroDivisionError):
NameError: name 'dhoni' is not defined
[9]
try:

    var=dhoni
    print(var)
except(ZeroDivisionError):
    print("bad")
except(NameError):
    print("good")
good

[10]
try:
    var="dhoni"+10
    print(var)
except(ZeroDivisionError):
    print("bad")
except(NameError):
    print("good")
except:
    print("helloo")
helloo

[11]
try:
    var="dhoni"+10
    print(var)
except(ZeroDivisionError,NameError):
    print("bad")
except:
    print("good")
good

[15]
try:
    var=10
    print(var)
except(ZeroDivisionError,NameError):
    print("bad")
except:
    print("good")
finally:
    print("new")
10
new

[16]
try:
    var=10/0
    ##var=10
    print(var)
except(ZeroDivisionError,NameError):
    print("bad")
except:
    print("good")
    
else:
    print("hello")
    
finally:
    print("new")
##bad
##new

else prints when try doesnt have any error... finally prints always at the end regardless of error or not in try.

this method cant be used in real time as there can be anynumber of error, cant possible to handle it all

[17]
try:
    var=10/0
    print(var)
except ZeroDivisionError as a:
    print(a)
division by zero

[19]
try:
    var=10+"a"
    print(var)
except TypeError as a:
    print(a)
unsupported operand type(s) for +: 'int' and 'str'

[20]
try:
    var=10+"a"
    print(var)
except Error as a:
    print(a)
---------------------------------------------------------------------------
TypeError Traceback (most recent call last)
<ipython-input-20-57ee8966f8e7> in <module> 1 try: ----> 2 var=10+"a" 3 print(var)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
During handling of the above exception, another exception occurred:
NameError Traceback (most recent call last)
<ipython-input-20-57ee8966f8e7> in <module> 2 var=10+"a" 3 print(var) ----> 4 except Error as a: 5 print(a)
NameError: name 'Error' is not defined
[24]
try:
    ##var=10+"a"
    ##var=10/0
    var=dhoni
    print(var)
except Exception as a:
    print(a)
name 'dhoni' is not defined

[25]
try:
    def fun (a,b):
        print(a+b)
    fun()
    
except Exception as a:
    print(a)
    
fun() missing 2 required positional arguments: 'a' and 'b'

[3]
try:
    var=10
    if(var>5):
        ##raise TypeError
        raise Error
        
except:
    print("good")
good

[9]
try:
    var=10
    if(var>5):
        raise TypeError ("bad")
except TypeError as a:
    print(a)
bad

[10]


try:
    var=10
    if(var>5):
        raise Exception ("bad")
except Exception as a:
    print(a)
bad

[11]
class Error(Exception):
    var="bad"

try:
    var=10
    if(var>5):
        raise Error
except Error as a:
    print(a.var)
bad


