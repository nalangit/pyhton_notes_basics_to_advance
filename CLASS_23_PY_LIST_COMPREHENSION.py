

                                                ##list comprehension

                          
var=[10,21,22,33,44]
a=[]
for x in var:
    a.append(x)
print(a)


##var=[10,21,22,33,44]
##a=[1,23,4,56]
##for x in var:
##    a.append(x)
##print(a)
print("========nxt prg=============2")
 
var=[10,7,8,9,49]
z=[x for x in var ]
print(z)


print("========nxt prg=============2")

var=[10,7,8,9,49]
a=[]
for x in var:
    b=x**2
    
    a.append(b)
print(a)


print("or or")
var=[10,7,8,9,49]
a=[]
for x in var:
    a.append(x**2)
print(a)




print("or or")

    
var=[10,7,8,9,49]
z=[x**2 for x in var]
print(z)

print("========nxt prg=============3")
## to print yhe even num alone
var=[10,7,8,9,49,6,8,3,4,14,44]
a=[]
for x in var:
    if(x%2==0):
        a.append(x)
print(a)

print("or,or")

var=[10,7,8,9,49,6,8,3,4,14,44]
z=[ x  for x in var if(x%2==0)]
print(z)

print("========nxt prg=============4")
## without giving input get out put divisible by 5 like 5,,15,20,25,30
a=[]
for x in range(1,6):
    a.append(x*5)
print(a)


print("copm1")
z= [x*5 for x in  range(1,6)]
print(z)

print("========or,or=========")

b=[]
for x in range(1,6):
    for y in range(5,6):
        b.append(x*y)
print(a)
print("comp2")

z=[x*y for x in range(1,6) for y in range(5,6) ]
print(z)


print("=====nxt prg=======6")
 
