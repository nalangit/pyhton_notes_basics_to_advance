
### class 10 apr 26 for loop & operators


##print even elements in a variable
##% -modulo (to get remainder in division)
##! -not equal to

var = "india"
a=0
for x in var:
    if(a%2==0):
        print(x)
    a=a+1
    
## Result -->

##I
##d
##a

print("nxt prg 2")

## Print odd number in Variable.

## 1 way of method
var="india"
a=1
for x in  var:
     if(a%2==0):
         print(x)
     a=a+1
    
## Result --> I-0,N-1,D-2,I-3,A-4

##n
##i

print("nxt prg 3")


##2nd type print odd index letters


var="india"
a=0
for x in var:
    if(a%2!=0):
        print(x)
    a=a+1

    
    ## Result --> I-0,N-1,D-2,I-3,A-4

##n
##i

print("nxt prg 4")

var="india"
for x in enumerate(var):   ##enumerate()is a built in function in python which is used to count the iterations
    print(x)


    ##Result
##(0, 'I')
##(1, 'n')
##(2, 'd')
##(3, 'i')
##(4, 'a')


print("nxt prg 5")


var="india"
for x,y in enumerate(var):
    print(x)
    print(y)

##Result
##0
##I
##1
##n
##2
##d
##3
##i
##4
##a

## Print even and odd number by using enumerate
print("nxt prg 6")
var="india"
for x,y in enumerate(var):
    if(x%2==0):
        print(y)

        ##by odd method

print("nxt prg 7")
var="india"
for x,y in enumerate(var):
    if(x%2!=0):
        print(y)

print("nxt prg 8")
 ## EVEN
var=["dhoni","kholi",'yuvi','jadu']
for x,y in enumerate(var):
    if(x%2!=0):
        print(y)

        
print("nxt prg 9")
    
##ODD
var=["dhoni","kholi",'yuvi','jadu']
for x,y in enumerate(var):
    if(x%2==0):
        print(y)
