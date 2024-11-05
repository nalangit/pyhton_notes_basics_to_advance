#POLYMORPHISM





class apple:
    def type(self):
        print("fruits")
        

    def color(self):
            print("red")

class tomato:
    def type(self):
        print("veg")

    def color(self):
            print("tom red")

a=apple()
a.type()
a.color()


b=tomato()
b.type()
b.color()

print("---------------------------------------------------------------2")


#ploymorphism can be done only when if DIFFERENT CLASS HAVE SAME FUNCTION NAME


class apple:
    def type(self):
        print("fruits")
        

    def color(self):
            print("red")

class tomato:
    def type(self):
        print("veg")

    def color(self):
            print("tom red")

def fun(obj):
    obj.type()
    obj.color()
c=apple()
d=tomato()
fun(c)
fun(d)


print("---------------------------------------------------------------3")
#class& static method  ------------


##class new:
##    def __init__(self,age,salary):
##        self.a=age
##        self.b=salary
##        
##    def fun (self):
##        print(self.a,self.b)
##
##    def fun1(salary):
##      if(salary>5000):
##          print("valid")
##c=new(10,10000)
##c.fun()
##c.fun1(7000)

##10 10000
##Traceback (most recent call last):
##  File "D:/NAL_STUDY_MATERIAL/BPY_MATERIAL/BPY_NOTES/CLASS_28_PY_POLYMORPHISM_MAY_27.py", line 78, in <module>
##    c.fun1(7000)
##TypeError: new.fun1() takes 1 positional argument but 2 were given
##


#=============DECORATERS ------------->@



class new:
    def __init__(self,age,salary):
        self.a=age
        self.b=salary
        
    def fun (self):
        print(self.a,self.b)

    @staticmethod
    def fun1(salary):
      if(salary>5000):
          print("valid")
c=new(10,10000)
c.fun()
c.fun1(7000)


##output:
##10 10000
##valid


print("nxr-----------------4")
##
### DECORATOR-----------> CLASS METHOD
##
##class new:
##    def __init__(self,age,salary):
##        self.a=age
##        self.b=salary
##        
##    def fun (self):
##        print(self.a,self.b)
##
##        
##     @staticmethod
##      def fun1(salary):
##      if(salary>5000):
##  
##
##          
##    @classmethod
##    def fun1(cls,age,salary):
##        return cls(age,salary)
##c=new(10,10000)
##c.fun()
##c.fun1(7000)
##
##
##d=new.fun1(35,40000)
##d.fun()
##
###35 40000



#STATIC METHOD:--------------@staticmethod===decorator

class new:
    def __init__(self,name,salary):
        self.a=name
        self.b=salary

    def fun(self):
        print(self.a,self.b)

    def fun1(self,gender):
        print(self.a,self.b,gender)
        
    @staticmethod
    def fun2(salary):
        if(salary>5000):
            print("valid")

            
c=new("don",40000)
c.fun()

c.fun1("male")
c.fun2(8000)

##CLASS METHOD:------@classmethod

class new:
    def __init__(self,name,salary):
        self.a=name
        self.b=salary

    def fun(self):
        print(self.a,self.b)

    def fun1(self,gender):
        print(self.a,self.b,gender)
        
    @staticmethod
    def fun2(salary):
        if(salary>5000):
            print("valid")
            
    @classmethod
    def fun3(ref,name,salary):
         return ref(name,salary)

            
c=new("don",40000)
c.fun()

c.fun1("male")
c.fun2(8000)


d=new.fun3("kholi",3000)
d.fun()


# classmethod is used to modify the class state that would apply accross all the instance of the class.
# classmethod is used  to get input and pass it to the other init functions.

class new:
    def __init__(self,name,salary):
        self.a=name
        self.b=salary

    def fun(self):
        c=self.a + self.b
        print(c)

    def fun1(self,gender):
        print(self.a,self.b,gender)
  
            
    @classmethod
    def fun3(ref,name,salary):
         return ref(name,salary)

d=new.fun3(10,20)
d.fun()
