## class7                 SET

#1) declaration {  ,   , }......set is an unordered collection of multiple datatypes

var={"dhoni","yuvi","abd",7,8}
print(var)
print(type(var))


#o/p: {'azar', 'mc', 6, 8, 'dhoni', 'abd'}
      #<class 'set'>

#2)not an array

#3) slicing.......slicing cannot be performed because the  elements values will be changed(unordered)

#var ={"dhoni","yuvi",7,8}
#print(var[1])



#Traceback (most recent call last):
 # File "D:/NAL_STUDY_MATERIAL/BPY_MATERIAL/BPY_NOTES/CLASS_7_PY_SET.py", line 18, in <module>
    #print(var[1])
#TypeError: 'set' object is not subscriptable


#5) manipulations

var ={"dhoni","yuvi",7,8}
var.add(10)
print(var) ## 4...set is mutable.....only through manipulations....not throug sclicing

var ={"dhoni","kholi",10,9,'azar'}
var.pop()
print(var) ## .pop will remove the random elements....it wont worklike list


var ={"dhoni","kholi",10,9,'azar'}
var.remove(10)
print(var)   ## o/p{'azar', 'kholi', 9, 'dhoni'}
## .remove() is used to remove the particular element in the set

var ={"dhoni","kholi",10,9,'azar'}
var.clear()
print(var)  ##o/p set()

var ={"dhoni","kholi",10,9,'azar'}
print(len(var))

##var ={"dhoni","kholi",10,9,'azar'}
##del(var)
##print(var)
##o/p NameError: name 'var' is not defined. Did you mean: 'vars'?

var =["dhoni","kholi",10,9,'azar']
a=set(var)
print(a)

var ={"dhoni","kholi",10,9,'azar'}
a=list(var)
print(a)


## adding element in converted list to set 
var =["dhoni","kholi",10,9,'azar']
a=set(var)
print(a)
a.add(10)
print(a) ## in set duplicate elements are not allowed

var =["dhoni","kholi",10,9,'azar']
a=set(var)
print(a)
a.add(1)
print(a)## a element which dosent present in the set can be added

var =["dhoni","kholi",10,9,'azar']
var.append(10)
print(var)



##var =["dhoni","kholi",10,9,'azar']
##a=frozenset(var)
##print(a)
##a.add(11)
##print(a)


 ##o/p: AttributeError: 'frozenset' object has no attribute 'add'



##frozen set is immutable.....but set is mutable




