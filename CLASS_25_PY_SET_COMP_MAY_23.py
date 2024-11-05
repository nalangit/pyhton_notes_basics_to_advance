##                                  SET_COMP_MAY_23::


var=[10,7,2,5]
a=set()
for x in var:
    a.add(x)
print(a)

z={x for x in var}
print(z)

#o/p
##{10, 2, 5, 7}
##{10, 2, 5, 7}
print("============22222222222222==============")

var=[10,7,2,5]
a=set()
for x in var:
    if x%2==0:
        a.add(x)
print(a)
     
var=[10,7,2,5]
z= { x for x in var if x%2==0}
print(z)


##o/p:
##{10, 2}
##{10, 2}

##genrator comprehension
  
var=[10,7,2,5,6]
z=(x for x in var if(x%2==0))
print(z)
for x in z:
    print(x)
