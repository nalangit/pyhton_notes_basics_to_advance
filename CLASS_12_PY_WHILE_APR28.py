##CLASS_12: WHILE .....PASS AND CONTINUE
print("nxt prg1")
var="india"
for x in var:
    if(x=="d"):
        pass
    print(x)

print("nxt prg2")
var="india"
for x in var:
    if(x=="d"):
        continue
    print(x)


print("nxt prg 3")

var=[10,7,3,5,4]
a=0
for x in var:
    a=a+x
print(a)

print("nxt prg 4")
##sum of.....
var=[10,7,3,5,4]


print("nxt prg 5") # sum of diigtts

var=586
a=0
while(var>0):
    dig=var%10
    a=a+dig
    var=var//10
print(a)






#var="586"
#a=list(var)
#print(a)
##GETING INPUT DYNAMICALLY IN FOR LOOOP
var=input("enter your name:")
print(var)
print(type (var))


var=int(input("enter your name:"))
print(var)
print(type (var))

