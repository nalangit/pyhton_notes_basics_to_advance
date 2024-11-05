
                                                                   ## LIST datatype___________12.04.2022


## list is  a collection of one or more element ,which are seprated by commas [,]and enclosed within square bracket[]
## eg: var =["dhoni","abd",7,49]

## 1) [  ,  ] _____list
##  2) NOT an array_____array  is also capable of many elements but only consists of element which has same datatype,,, but list is capable of containing many datatype...eg:[str, int, str]
##  3) slicing
## 4) mutable or immutable.............list is mutable
## 5)LIST MANIPULATION



var =["dhoni","abd",7,49]
print(var)
print(type(var))

print("_________________________break____________________________")

##3) slicing "kholi from list"
var =["dhoni","kholi",7,49]
print(var[1])
print(var[-3])
print(var[1:2])
print(var[1:-2])
print(var[-3:-2])
print(var[-3:2])

print("_________________________break____________________________")


var =["nal", "al","kill",5 ,88,99] ## to print kill
print(var[2])
print(var[-4])
print(var[2:3])
print(var[2:-3])
print(var[-4:-3])
print(var[-4:3])


##to print h from
"kholi"
var =["dhoni","kholi",10,8]
print(var[1][1])
print(var[1][-4])
print(var[1][1:2])
print(var[1][1:-3])
print(var[1][-4:-3])
print(var[1][-4:2])
print("_________________________break____________________________")

##4___________ mutable or immmutable
var =["dhoni","kholi",10,8]
var[1]= "yuvi"
print(var) ## when we modify a list , the changes are reflected in the in original memory, SO LIST IS MUTABLE............................


##var[1][1] ="m"
##print(var)   type error: 'str' dose not support item asssignment
print("_________________________break____________________________")



##5) list manipulation ______attributes used in string will not work in list.... even though the list full of string
##_______________________________list has sepatrate attributes.....


var =["dhoni","kholi","yuvi","azar"]
var.append("jadu")
print(var)

##var =["dhoni","kholi","yuvi","azar"]
##var.append("jadu","rahul")
##print(var) ______________________o/p error>>>>>>>>>>>>append  can add only one element


var =["dhoni","kholi","yuvi","azar"]
var.append(["jadu","rahul","mcculllum"])
print(var) ##o/p ['dhoni', 'kholi', 'yuvi', 'azar', ['jadu', 'rahul', 'mcculllum']]
## o/p will be in the form of nested list ,so we cannot add multiple element in list using .apppend()


print("_________________________break____________________________ extend")


##__________________________________.extend() attribute is used to insert multiple elements

var =["dhoni","kholi","yuvi","azar"]
var.extend(["jadu","rahul","mcculllum"])
print(var)

print("break________________________________")
## .pop() attribute is used to pop out(remove) the element in list

var =["dhoni","kholi","yuvi","azar"]
var.pop()
print(var)


print("_________________________break____________________________")

var =["dhoni","kholi","yuvi","azar"]
var.pop(2)## index value to remove particular element
print(var)

print("_________________________break____________________________")



##.remove()
var =["dhoni","kholi","yuvi","azar"]
var.remove("yuvi")   ## top remove a particular element in list
print(var)
print("_________________________break____________________________")

var =["dhoni","kholi",10,"azar"]
var.remove(10)   ## top remove a particular element in list
print(var)


var =["dhoni","kholi","yuvi","azar"]
var.insert(1,"jadu")   ## top insert a particular element in list at a patricular index place
print(var)               ## syntax: variable_name.insert(index_value , argument) arguement may be a str,int, float



var =["dhoni","kholi","yuvi","azar"]
var.sort()             ## to sort or arrange the list in asscending order
print(var)              ##o/p: ['azar', 'dhoni', 'kholi', 'yuvi']





var =["dhoni","kholi","yuvi","azar"]
var.sort(reverse = True)    ## to sort or arrange the list in descending  order
print(var)                  ##o/p:   ['yuvi', 'kholi', 'dhoni', 'azar']

var =["dhoni","kholi","yuvi","azar"]
print(sorted(var))              ## sorted is a keyword used in list...to sort in asscending order

var =["dhoni","kholi","yuvi","azar"]
print(sorted(var, reverse = True))   ## to sort in desending order



var =["dhoni","kholi","yuvi","azar"]
print(len(var))


var =["dhoni","kholi","yuvi","azar"]
var.clear()
print(var)

var =["dhoni","kholi","yuvi","azar"]
print(var.clear()) ##o/p: NOne syntax shouldnt be like this for .clear()

var =["dhoni","kholi","yuvi","azar"]
del(var)
print(var)
## o/p :: error...Traceback (most recent call last):
  ##File "D:\NAL_STUDY_MATERIAL\BPY_MATERIAL\BPY_NOTES\CLASS_4_PY.py", line 151, in <module>
    ##print(var)
##NameError: name 'var' is not defined. Did you mean: 'vars'?


