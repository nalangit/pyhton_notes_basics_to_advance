
var = "india"
print(var)
print(type(var))

var =10.5
print(var)
print(type(var))


var1 =10
var2 =20
print(var1+var2)

var1 ="10"
var2 ="20"
print(var1+var2)


var1 = 10
var2 =5.5
print(type(var1 +var2))



var1 = "dhoni"
var2 = 7
print(var1 )


var1 = "dhoni"
var2 = 7
print(var1 + str(var2))


##type1
var1= "india"
var2 =350
var3 ="srilanka"
var4 =39
var5=9
print(var1,"score",str(var2),"runs against ",var3,"in",str(var4),"overs with",str(9),"extras")

##type2

var="samsung"
print(var[2],var[4])



var ="india" ##...................negative indexing
print(var[-3])

var ="samsung" ##..................................print m and u in samsung using NEGATIVE INDEXING
print(var[-5])
print(var [-3])
print(var[1:4]) 


var ="ganguly"
print(var[3:6]) ##............to print gul
print(var[2:5]) ##...............to print ngu
print(var[-4:-1])

var ="ganguly"
print(var[:-1])




var ="srilanka"
print(var[3]) ##......l
print(var[-5]) ##....l
print(var[-1]) ##.....a
print(var[7]) ##....a
                                                                ##.................. to print in 4 different ways...............

print(var[3:6]) ##.............p-p.....idex :value
print(var[3:-2]) ##............p-n.....index:value of next digit
print(var[-5:-2]) ##...........n-n.....value:value of next
print(var[-5:6]) ##............n-p.....value: value

## to print LIR in reverse
print(var[-4:-7])




var="srilanka"
print(var[::-1]) ###....... o\p aknalirs
print(var[::-2]) ##......rlna
print(var[::3]) 



var = "india intention india"
print(var.count("in",3))

var = "india intention india"
print(var.count("in",8,18)) 

var = "india intention india"
print(var.find("in",3)) 

var = "india intention india"
print(var.find("in",8,20))


print(var[6:8])



var = "india intention india"
print(var.index("in"))    ##...o/p  0
print(var.index("in",3))  ##...o/p 6
print(var.index("in",8,20)) ##  ...o/p 16


var ="westindies"
print(var.find("z"))  #.....o/p : -1  [index value will never be a negative value ]
print(var.index("z"))


var = ("!india is my country!")
print(var.strip("!"))  ## strip 



var = ("!india is my country!")
print(var.strip("is"))



var = ("india is my country")
print(var.upper())
print(var.lower())
print(var.title())
print(var.capitalize())


var = ("india is my country")
print(var.isupper())
print(var.islower())
print(var.istitle())


var = "india is my country"
print(var.startswith("india"))
print(var.endswith("country"))
print("is" in var)



var = "india"
print(var.replace("n","m"))##....ITS COPY OF THE MEMORY.....

var = "india"
var=var.replace("n","m") 



var =["dhoni","abd",7,49]
print(var)
print(type(var))




##3) slicing "kholi from list"
var =["dhoni","kholi",7,49]
print(var[1])
print(var[-3])
print(var[1:2])
print(var[1:-2])
print(var[-3:-2])
print(var[-3:2])




var =["nal", "al","kill",5 ,88,99] ## to print kill
print(var[2])
print(var[-4])
print(var[2:3])
print(var[2:-3])
print(var[-4:-3])
print(var[-4:3])



var =["dhoni","kholi",10,8]
var[1]= "yuvi"
print(var)


var =["dhoni","kholi","yuvi","azar"]
var.extend(["jadu","rahul","mcculllum"])
print(var)



var =["dhoni","kholi","yuvi","azar"]
var.insert(1,"jadu")   ## top insert a particular element in list at a patricular index place
print(var)               ## syntax: variable_name.insert(index_value , argument) arguement may be a str,int, float



var={"name":"dhoni","age":35}
print(var)
print(type(var))


var1={1:"dhoni",2:10}
print(var1)
print(type(var1))

print(var["name"])
print(var1[2])
print(var["age"])




var3={"name":["dhoni","kohli"],"age":["40","30"]}
##print(var3)
##print(type(var3))
print(var3["name"][1][2])

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




var4={"name":{"age":10,"gender":"male"},"command":"no"}




print(var4["name"]["gender"])
print (var4)

var["name"]="kohli"
print(var)






var5={"name":["dhoni","jaddu","bravo"],"age":[40,35,37]}
                                              
var5["name"][2]="dj"
print(var5)



a=[10,11,12]
b=[13,14,15]
a.extend(b)
print(a) 




##since list is mutable. have to execute the variable 

var7={"name":"dhoni","age":10}
var8={"name":"kohli","age":20}

var7.get




var={"name":"dhoni","age":10}
var.pop("name")
print(var)

var={"name":"dhoni","age":10}
var.pop("age")
print(var)

var={"name":"dhoni","age":10}
var.remove("age")
print(var)


var="ganguly"
for x in var:
    if(x=="g"):
      print('present')
    elif (x!="g"):
      print("not present")
      
      
      
var="gangulyl"
for x in var:
   case "g"|"l":
        print('present')
   case -:
      print("not present")
        
        
        
var = "gangulyl"
for x in var:
    match x:
        case "g" | "l":
            print("present")
        case _:
            print("not present")
