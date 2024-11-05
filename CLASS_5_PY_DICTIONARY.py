                                        ##dictionary







##1. synatx=={key:value,key:value}---key value is seperated by colon and key value pairs are seperated by comma

##dict is a collection of more than one data, consists of key value pairs enclosed in curly brackets. the key and value  are seperated by colon and multiple key value pairs are seperated by comma. 


##2. dictinary is not an array--array is collection of data with same data type, but dict can have collection of data 
    ##with multiple data types
    
##3. slicing-- slicing cant be performed directly... need to take the value out first and then perform slicing.

##4. dict is mutable, any changes made in dictionary is reflected in original memory




var={"name":"dhoni","age":35}
print(var)
print(type(var))


var1={1:"dhoni",2:10}
print(var1)
print(type(var1))

print(var["name"])
print(var1[2])
print(var["age"])

print(var["name"][1])
print(var.items())

var3={"name":["dhoni","kohli"],"age":["40","30"]}
##print(var3)
##print(type(var3))
print(var3["name"][1][2])

##print(var3["name"][1])


var4={"name":{"age":10,"gender":"male"},"command":"no"}




print(var4["name"]["gender"])
print (var4)

var["name"]="kohli"
print(var)



##var["name"][1]="m"
##print(var)





##dict is mutable.... string is immutable

var5={"name":["dhoni","jaddu","bravo"],"age":[40,35,37]}
                                              
var5["name"][2]="dj"
print(var5)

var6={"name":{"captain":"dhoni"}}


print(var6.keys())
print(var6.values())

print(var6.items())

##print(var6["gender"])

###print(var6.get("gender"))

##get attribute gives back none as output doesnt give keyerror. so need to fetch values using get is preffered.

##directly fetching values shud be done only if we are sure the key is present in the dict

a=[10,11,12]
b=[13,14,15]
a.extend(b)
print(a) 

##since list is mutable. have to execute the variable 

var7={"name":"dhoni","age":10}
var8={"name":"kohli","age":20}

var7.get("age")

## __________________________________ dictionary


var ={"name":{"age":10,"gender":"male","command" :"no"}}
print(var["name"]["gender"])

var ={"name":{"age":10,"gender":"male","command" :"no"}}
print(var["name"]["gender"])
print(var["name"]["gender"][1])

var={"name":"dhoni","age":40}
var["name"] ="kholi"
print(var)  ## dictionary value is mutable

####var={"name":"dhoni","age":40}
##var["name"][1] ="m"
##print(var) ##___________________string is immutable

var={"name":["dhoni","sanga","abd","kholi"],"age":40}
var["name"][3] ="mccullum"
print(var)

var={"name":["dhoni","sanga","abd","kholi"],"age":40}
var["name"][3] ="mccullum"
var["age"] ="mccullum"
print(var)


var={"name":{"dhoni":1,"sanga":2,"abd":3,"kholi":5},"age":40}
var["name"]["kholi"] ="4"
print(var)



##_________________________________## 5)dictionary manipulations"
print("##_________________________________## 5)dictionary manipulations")
var={"name": "dhoni","age":10}
print(var.keys())
print(var.values())

var={"name": "dhoni","age":10}
print(var.items())

##var={"name": "dhoni","age":10}
##print(var["gender"])  errror: key error





var={"name": "dhoni","age":10}
print(var.get("gender"))
print(var.get("age"))  ##.get() attribute is used to get output ...it will not show error

print("------------------------>")

a=[10,11,12]
b=[13,14,15] ## adding two list
print(a+b)
a.extend(b)
print(a)
a.append(b)
print(a)

var={"name":"dhoni","age":10}
var1={"name":"kholi","age":20}
var.update(var1)  ## duplicate keys are not allowed
print(var)   ##o/p{'name': 'kholi', 'age': 20}

##same key should be declared

var={"name":"dhoni","age":10}
var1={"name":"kholi","age1":20} ##changed key value
var.update(var1)
print(var)  ##o/p{'name': 'kholi', 'age': 20}

var={"name":"dhoni","age":10}
print(len(var))

##var={"name":"dhoni","age":10}
##var.pop()
##print(var)

var={"name":"dhoni","age":10}
var.pop("age")
print(var)

##var={"name":"dhoni","age":10}
##var.remove("age")
##print(var)

var={"name":"dhoni","age":10}
var.clear()
print(var)

##var={"name":"dhoni","age":10}
##del(var)
##print(var)  del will delete the var memory

var={"name":"dhoni","age":30}
print(var["name"].count("d"))
print(var["name"].index("o"))
print(var["name"].find("o"))



var ={"name":["dhoni","yuvi"],"age":[10,20]}
var["name"].append("jadeja")
print(var)


var ={"name":["dhoni","yuvi"],"age":[10,20]}
var["name"].insert(1,"jadeja")
print(var)

var ={"name":["dhoni","yuvi"],"age":[10,20]}
var["name"].pop()
print(var)

var ={"name":["dhoni","yuvi","mcay","bale","nal"],"age":[10,20]}
var["name"].sort()
print(var)


var ={"name":["dhoni","yuvi","mcay","bale","nal"],"age":[10,20]}
var["name"].sort(reverse=True)
print(var)


var ={"name":["dhoni","yuvi","mcay","bale","nal"],"age":[10,20]}
var["name"][0]="abd"
print(var)



