#------------------------COLLECTIONS  library------------------------

  
##1- NAMED TUPLE

##2- DEQUE

##3- CHAIN MAP

##4- COUNTER
 
##5- ORDERED LIST

##6- DEFAULT DICT
#---------------------------------------------------------------------------------------

#1-named tuple------------is als immutable

from collections import namedtuple
 
b=namedtuple("stud",["name","age","gender"])

c=b("gon",40,"male")
print(c)




print("#---------------------------------------------------------------------------------------2")


#print-- 40 alone

from collections import namedtuple
 
b=namedtuple("stud",["name","age","gender"])

c=b("gon",40,"male")
print(c[1])     #--------------- printing value using index-----1

print(c.gender) #------------ printing value using list elements-----2

print(getattr(c,"name")) #------printing value using attribute= attr-----3


print(c._fields)  #--------------printing value using field------4

print(c._asdict()) # to convert output as dict--5

di={"name":"yuvi","age":50,"gender":"male"}

print(b(**di)) #------------- from dict to namedtuple---6

print(c._replace(name ="rahul")) # to replace the  value of the name-----7



##40----1
##male-----2
##gon----------3
##('name', 'age', 'gender')----------4
#{'name': 'gon', 'age': 40, 'gender': 'male'}----------5
#stud(name='yuvi', age=50, gender='male')----------6
#stud(name='rahul', age=40, gender='male')---------7
print("#---------------------------------------------------------------------------------------3")

from collections import namedtuple
b=namedtuple("stud",["name","age","gender"])
li=["ko",56,"male"]
print(b._make(li))



#stud(name='ko', age=56, gender='male')

print("#---------------------------------------------------------------------------------------4")

