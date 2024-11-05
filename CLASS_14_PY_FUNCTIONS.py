##  class 14 03 ,may   functions
## it is group of statements that can perfotm specific task.
## function is executed only if we call that function by its original name(function name)

## Advantages of function
## 1--secure(code is secure in function, because it executed only when it is called)
## 2--compact___ ordered or arranged
###3 --code reusability----can use the same code for different inputs in different tasks
## better understanding of the code


## function syntax
## def FUNCTION_NAME ():
    ##statements
   #FUNCTION_NAME()
           

## function with zero arguement
def new():
    print("success")
new()
print('nxt -------------------------2')

def all():
    print("nalan")
all()
print('nxt -------------------------3')

## function with one  arguement
#def fun(a):
#    print("ammmber")
#fun()
def  fun(a):
    print(a)
fun(10)

def fan(a):
    print(a)

fan("nalan")
print('nxt -------------------------4')
## function with 2 arguements
def sum(a,b):
    print(a+b)
sum(10,20)
print('nxt -------------------------5')
## function with 3 arguements
#def add(a,b,c):
#   print(a+b+c)
#add(10,20)
# add(10,20)
#TypeError: add() missing 1 required positional argument: 'c'

def add(a,b,c):
    print(a+b+c)
add(10,20,30)
print('nxt -------------------------6')

def cric(a,b):
    print(a,"scored",b,"runs")
cric("dhoni",100)
##dhoni scored 100 runs
print('nxt -------------------------7')

def cric(a,b):
    print(a,"scored",b,"runs")
cric(100,"dhoni")
##100 scored dhoni runs
print("nxt day--------------------------8")

##class14 04,may


def prt(a,b):
    print(a,"has a avg :",b)
prt("dhoni",50)

print('nxt -------------------------9')
def prt(a,b=50):
    print(a,"has a avg :",b)
prt("dhoni")

print('nxt -------------------------10')

#def prt(a="dhoni",b):
 #   print(a,"has a avg:",b)
#prt(50)
 #### syntax:: invalid arguement because a value is replaced by 50 and  b has value...............

def prt(b,a='dhoni'):
    print(a,"has a avg :",b)
prt(50)
print('nxt -------------------------11')
def prt(b,a):
    print(a,"has a avg :",b)
prt(a= "dhoni",b=50)
## even if the order of the parameter is unorder ,while declaring parameter  value we have assign value corectly
print('nxt -------------------------12')

def ele(a):
    print(a)
ele(10)
ele(40)

print('nxt -------------------------13')
def val(*a):
    print(a)
    print(type(a))
val(10,20)
val(56,98,98,45,36)
#when we assign *a the group of elements assigned values here is converted to tuple>>
#o/p
#(10, 20)
#<class 'tuple'>
#(56, 98, 98, 45, 36)
#<class 'tuple'>


print('nxt -------------------------14')
def val(**a):
    print(a)
    print(type(a))
val(a=30)
val(b=23,c=90,d=50,e=67)
val(f=90,g=66,h=22)


##{'a': 30}
##{'b': 23, 'c': 90, 'd': 50, 'e': 67}
##{'f': 90, 'g': 66, 'h': 22}

## when we assign **a the group of elements assigned values here is converted to dict.......>>
def add(a,b):
   
    sum= a+b
    print(sum)
    c=sum+10
    print(c)
   
#add(10,20)
a=int(input('enter a val:'))
b=int(input('ente b val:'))
print(a)
print(b)
add(a,b)
print('nxt -------------------------15')

#def fun(a,b):
#    print(a+b)
#c=fun(10,20)
#print(c+10)
#o/p::30
#Traceback (most recent call last):
 # File "D:\NAL_STUDY_MATERIAL\BPY_MATERIAL\BPY_NOTES\CLASS_14_PY_FUNCTIONS.py", line 144, in <module>
  #  print(c+10)
  
#TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

print('nxt -------------------------16')
def fun(a,b):
    return a+b
c=fun(10,20)
print(c+100)


print('nxt -------------------------17')
def fun(a,b):
    print('success')
    print(a+b)
    return 'good'
fun(10,20)

##o/p :success
## 30
print('nxt -------------------------18')
def fun(a,b):
    print('success')
    print(a+b)
    return 'good'
print(fun(10,20))
#o/p:sucess
#30
#good
print('nxt -------------------------19')
def fun(a,b):
    print('success')
    print(a+b)
    return 'good'
a=fun(10,20)
print(a)
#o/p:sucess
#30
#good

print('nxt -------------------------20')
def fun(a,b):
    print('success')
    return 'good'
    print(a+b)
    
a=fun(10,20)
print(a)
#o/p::::success
        #good
print('nxt -------------------------21')
def fun(a,b):
    return 'good'
    print('success')
    
    print(a+b)
    
    
a=fun(10,20)
print(a)
#o/p::::good
print('nxt -------------------------22')
##RETURN----------return is a statement which is end of the statement in function.........even if u give a lot of statements after return it wont be printed here.................... 
