a=2
if(a<10):
    print(a)
    a=a+2
 # using if condition the program will be running only one time , for A alone---------it will not work incremental values
 # but in WHILE LOOP it will running the program untill the condition satisfiesa=2


print("---------------------------------------2")

a=2
while(a<10):
    print(a)
    a=a+2
    
print("------------------------3")

#REVERSING A INTEGER

var=586
a=0
while(var>0):
    dig=var%10
    a=a*10+dig
    var=var//10
print(a)

print("--------------------3.1")

#not by while loop:
var=586
var1=str(var)
print(var1[::-1])

print("----------------------4")

var="india"
for x in var:
    if(x=="d"):
     print(x)

##var="india"
##for x in var:
##    while(x=="d"):
##     print(x)

#for this the output will be infinite number of d


#  if we are using while condition means ,the condition should be finite........like greater than,less than,not equal to are FINITE condition examples


print("-------------------------------------5")
#suming the int
var=586
a=0
while(var>0):
    dig=var%10
    a=dig+a
    var=var//10
print(a)
