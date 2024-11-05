##                    CLASS-MAY-25
        ##class==== class is a way or procedure for creating an object
        ##IT IS A BLUEPRINT OF OBJECT

##ADVANTAGES OF CLASS:
##    security
##    code readability===better understanding
##    code reuseability
##    compact code
##    easy way of understanding
##    simplified coding


## class is also collection of one or more related statements,
##  it can be executed only when we call it using its name

##types of classes:
##  1.unbounded class----------
##  2.bounded class


##  1. unbounded class:

class new:
    var=10
    print(var)
new() # new===== no need of bracket like function

print("==========or=========1")



class new:
    var=10
    print(var)
new


print("==========or=========2")


class new:
    var=10
print(new.var)



print("==========or=========3")

##  function inside  a class

class don:
    def fun():
        print("good")
don.fun()


print("==========or=========4")


## class+ fun+ arguement
class new:
    def fun(a):
        print(a)
new.fun(100000000)



print("==========or=========5")
##  to add two numbers using CLASS & FUNCTION:




##class add:
##    def plus(a,b):
##        print(a+b)
##
##a=int(input("ent a:"))
##b=int(input("ent b:"))
##
##add.plus(a,b)


##with print statement:


class add:
    def sum(a,b):
        c=a+b
        print(c,"is sum of",a,"and",b)
add.sum(2,3)




print("==========or=========6")
##  to add two numbers using CLASS alone::


##class add:
##   a=int(input("ent num a:"))
##   b=int(input("ent num b:"))
##   print(a+b)
##
##add



print("==========or=========7")
##
####two function with same  function name
##
##class new:
##    def fun():
##        print("success")
##
##
##    def fun(a,b):
##        print(a+b)
##new.fun()
##
##TypeError: new.fun() missing 2 required positional arguments: 'a' and 'b'

## here what we have done is , we called the second fun [line by line excecution so it gose to 2nd function after it]
## while calling the fun we did not give any parameters ,sp the type error occurs
##

print("==========or=========8")

##two function with same  function name

##python is line by line execution so it replace 1st fun with 2nd fun

class new:
    def fun():
        print("success")


    def fun(a,b):
        print(a+b)
new.fun( 10,20)

print("==========or=========9")

## class & PRIVATE function============  use two underscore before function eg: __fun

##private option is used to eliminate fun

class new:
    def fun():
        print("success")


    def __fun(a,b):
        print(a+b)
new.fun()

print("==========or=========10")

## even if you call it using __ two underscore in while calling it wont run


class new:
    def fun():
        print("success")

        


    def __fun(a,b):
        print(a+b)
new.__fun()

##AttributeError: type object 'new' has no attribute '__fun'

print("============or===========11")
## to execute two function in a class only way  we have is to change the function name
class new:
    def fun():
        print("success")


    def fun1(a,b):
        print(a+b)
new.fun1(30,80)
