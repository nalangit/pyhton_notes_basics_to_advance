#-------------------------ENCAPSULATION__________JUNE-7---------------------------------


class person:
    def __init__(self,name,age=0):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
c=person("dhoni",40)
c.display()
print(c.name)
print(c.age)




print("----------------------------------------------2")





##class person:
##    def __init__(self,name,age=0):
##        self.name=name
##        self. __age=age
##    def display(self):
##        print(self.name)
##        print(self. __age)
##c=person("dhoni",40)
##c.display()
##print(c.name)
##print(c. __age)

##dhoni
##40
##dhoni
##40
##----------------------------------------------2
##dhoni
##40
##dhoni
##Traceback (most recent call last):
##  File "C:/Users/nalan/AppData/Local/Programs/Python/Python310/CLASS_29_PY_CLASS_ENCAPSULATION_JNUE7.py", line 35, in <module>
##    print(c. __age)
##AttributeError: 'person' object has no attribute '__age'



print("----------------------------------3-----")


class person:
    def __init__(self,name,age=0):
        self.name=name
        self.__age=age
    def display(self):
        print(self.name)
        print(self.__age)
        
    def getdata(self):
      print(self.__age)

    def putdata(self,age):
        self.__age=age
c=person("dhoni",40)
c.display()
c.putdata(35)
c.getdata()

##dhoni
##40
##35

