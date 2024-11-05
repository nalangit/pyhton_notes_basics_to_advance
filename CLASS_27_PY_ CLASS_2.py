


count=10
class new:
    count=20
    def fun(a,b):
        print(a+b)
new.fun(10,20)   #----------executing inside fun
print(new.count) #----------executing CLASS & COUNT===20
print(count)    #-----------executing COUNT=10

#output:
##30
##20
##10

print("nxt============1111")
  
count=10
class new:
    global count
    count = 20
    def fun(a,b):
        print(a+b)
new.fun(10,20)   #----------executing inside fun
##print(new.count) #----------
print(count)    #----------


print("nxt============2")


## INHERITANCE:                                            INHERITANCE  is part of unbounded class


##Inheritance allows us to define a class that inherits all the methods and properties from another class.
##
##Parent class is the class being inherited from, also called base class.
##
##Child class is the class that inherits from another class, also called derived class.
##
class old:
    def fun():
        print("success")

        
class new(old):
    def fun1(a,b):
        print(a+b)
new.fun()
new.fun1(10,20)

# child class has ability to access the parent class function
# but parent class has no right to access child class function


print("nxt============2")

#multilevel inheritance:

class a:
    def fun():
      print("class a")


class b(a):
    def fun():
      print("class b")




class c(b,a):
    def fun():
      print("class c")



class d(c,b):
    def fun():
      print("class d")

      
d.fun()


print("nxt==========3")

class a:
    def fun():
      print("class a")


class b(a):
    def fun():
      print("class b")




class c(b,a):
    def fun():
      print("class c")



class d(c,b):
    pass
      
d.fun()


print("nxt==========4")

class a:
    def fun1():
      print("class a")


class b(a):
    def fun2():
      print("class b")




class c(b,a):
    def fun3():
      print("class c")



class d(c,b):
    def fun4():
      print("class d")

d.fun1()

print("nxt==========5")

# method resolution order =MRO---------- error

##class a:
##    def fun1():
##      print("class a")
##
##
##class b(a):
##    def fun2():
##      print("class b")
##
##
##
##
##class c(b,a):
##    def fun3():
##      print("class c")
##
##
##
####class d(c,b): -------------  here the heritance order is changed so error will occur
##class d(b,c):
##    def fun4():
##      print("class d")
##
##d.fun1()



# method resolution order =MRO

##TypeError: Cannot create a consistent method resolution
##order (MRO) for bases b, c
##
##
print("nxt==========6")

##DISADVANTAGE:
 # NEED TO PASS ARGUEMENTS EACH AND EVRY TIME, MEMORY CPACITY IS EXTENDED

class new:
    def fun(ip,pwd):
        print(ip,pwd)
    def fun1(ip,pwd,code):
        print(ip,pwd,code)


new.fun("127.0.01.0","nal@")
new.fun1("127.0.01.0","nal@","ipconfig")

##--------------------------------------------------------------bounded class-----------------------------------------------------------------
##  creating object
#__init__=== initialize


##Python is an object oriented programming language.
##
##Almost everything in Python is an object, with its properties and methods.
##
##A Class is like an object constructor, or a "blueprint" for creating objects.
##



class new:
    def __init__(self,ip,pwd,code):
        self.a=ip
        self.b=pwd
        self.c=code
    def fun(self):
            print(self.a,self.b)

    def fun1(self):
         print(self.a,self.b,self.c)


#creating an object ===c
c=new("112.4..5.","nal@01","akasaa")
c.fun()
c.fun1()

##112.4..5. nal@01
##112.4..5. nal@01 akasaa
##



#---------------------------------------------------------------------------


# using particular varialble for particula function alone

# code variable

class new:
    def __init__(self,ip,pwd):
        self.a=ip
        self.b=pwd
        
    def fun(self):
            print(self.a,self.b)

    def fun1(self,code):
         print(self.a,self.b,code)


#creating an object ===c
c=new("112.4..5.","nal@01")

c.fun()
c.fun1("aaakasaa") # declare the value for variable as parameter....


#output:

##112.4..5. nal@01
##112.4..5. nal@01 aaakasaa
#---------------------------------------------------------------------------

# creating two objects:

class new:
    def __init__(self,ip,pwd,code):
        self.a=ip
        self.b=pwd
        self.c=code
    def fun(self):
            print(self.a,self.b)

    def fun1(self):
         print(self.a,self.b,self.c)


#creating an object ===c
c=new("112.4..5.","nal@01","akasaa")
d=new("1235677","wolve","tejasexp")
c.fun()
c.fun1()
d.fun1()

##112.4..5. nal@01
##112.4..5. nal@01 akasaa
##1235677 wolve tejasexp
##-------------------------------------------------------------------------------------------


class old:
    def __init__(self,name,age):
     self.a=name
     self.b=age

     
    def fun(self):
        print(self.a,self.b)

class new(old):
    def __init__(self,name,age):
        self.a=name
        self.b=age

    def fun1(self):
            print(self.a,self.b)
n=new("don",56)
n.fun()
n.fun1()


print("##------------------------------------------------------------------------------------")


##class old:
##    def __init__(self,name,age):
##     self.a1=name
##     self.b1=age
##
##     
##    def fun(self):
##        print(self.a1,self.b1)
##
##class new(old):
##    def __init__(self,name,age):
##        self.a=name
##        self.b=age
##
##    def fun1(self):
##            print(self.a,self.b)
##n=new("gon",56)
##n.fun()
##n.fun1()
##
##
##Traceback (most recent call last):
##  File "D:\NAL_STUDY_MATERIAL\BPY_MATERIAL\BPY_NOTES\CLASS_PY_27_ CLASS_2.py", line 329, in <module>
##    n.fun()
##  File "D:\NAL_STUDY_MATERIAL\BPY_MATERIAL\BPY_NOTES\CLASS_PY_27_ CLASS_2.py", line 319, in fun
##    print(self.a1,self.b1)
##AttributeError: 'new' object has no attribute 'a1'. Did you mean: 'a'?
##



print("##------------------------------------------------------------------------------------")

class old:
    def __init__(self,name,age):
     self.a1=name
     self.b1=age

     
    def fun(self):
        print(self.a1,self.b1)

class new(old):
    def __init__(self,name,age):
        old. __init__(self,name,age)
        self.a=name
        self.b=age

    def fun1(self):
            print(self.a,self.b)
n=new("gon",57)
n.fun()
n.fun1()

##gon 57
##gon 57

##have to mention [  old.__init__ function for child class to consider the
##init class of parent,else it take only init class of child

