#----------------------------------------ASSERT-        LOOPING        ---_______JUNE_9





def fun(a):
    if (len(a)>0):
        b=sum(a)
        c=b/len(a)
        print(c)
    else:
        print("empty list")

a=[]
fun(a)


#empty list
print("-------------------------------------------2")


def fun(a):
    if (len(a)>0):
        b=sum(a)
        c=b/len(a)
        print(c)
    else:
        print("empty list")

a=[10,7,2,5]
fun(a)

##6.0


print("-------------------------------------------3")

##
##def fun(a):
##    assert(len(a)>0),"list is empty"
##    b=sum(a)
##    c=b/len(a)
##    print(c)
##    
##a=[]
##fun(a)

## assert(len(a)>0),"list is empty"
##AssertionError: list is empty


print("-------------------------------------------4")


def fun(a):
    assert(len(a)>0),"list is empty"
    b=sum(a)
    c=b/len(a)
    print(c)
    
a=[10,34,56]
fun(a)

##33.333333333333336


print("-------------------------------------------5")



