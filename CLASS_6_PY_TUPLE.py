## class 6 tuples
  ##syntax for tuple:::::   variable_name =(str,int,str)  in a group of element on normal  bracket if the elements are separated by ,(comma) then it is tuple.

##1) syntax  (   ,  )
##2  not an array



var=("dhoni",7)
print(var)
print(type(var))


var1=("dhoni")
print(var1)
print(type(var1))

var1=("dhoni" ,)
print(var1)
print(type(var1))


## 3   slicing

var=("dhoni",7)
print(var[0])
print(var[-2])
print(var[0:1])
print(var[0:-1])
print(var[-2:-1])
print(var[-2:1])


##o/p:.........................while doing slicing if we use the index or negative value means,like first two function output will be in  str............if  we use n:p like that menas it will give o/p in datatype model
##dhoni
##dhoni
##('dhoni',)
##('dhoni',)
##('dhoni',)
##('dhoni',)

##4) mutable or immutable....it is immutable

#var =("dhoni",7)
#var[0]="yuvi"
#print(var)
#TypeError: 'tuple' object does not support item assignment


## 5 manipulation


##var =("dhoni",8,9)
##var.append("abd")
##print(var)

#Traceback (most recent call last):
  #File "D:/NAL_STUDY_MATERIAL/BPY_MATERIAL/BPY_NOTES/CLASS_6_PY_TUPPLE.py", line 50, in <module>
    #var.appens("abd")
#AttributeError: 'tuple' object has no attribute 'append'


##only two attributes are  there in tuple .count, .index

var =("dhoni",8,9,8)
print(var.count("dhoni"))
print(var.index("dhoni"))
print(var.count(8))
print(var.index(8))
