##def lam():
##   a= int(input("enter a dig"))
##   print(a)
##lam()

#lambda function is anonymous function___  anonymous___not defined by name

#syntax:  --- function_name= lambda a:a
#              print(function_name)


don = lambda a:a
print(don(10098765))

print("sqrt-------------------")

def lam(a):
  a=a**2
  print(a)


lam(10)

don=lambda a:a**2
print(don(10))

print("add-------------------")

def lam(a,b):
  a=a+b
  print(a)
  


lam(10,456)


don=lambda a,b:a+b
print(don(10,456))


print("=-----------------sqrt list")


def sqrt():
    var=[10,7,5,67,5]
    
    for x in var :
        x=x**2
        
        print(x)
        
        
        

sqrt()


var=[10,7,5,8,4,2,67,5]
sa=list(map(lambda x:x**2,var))
print(sa)


print("geting even -----------------------num from list")


var=[10,7,5,8,4,2,67,5]
ev=list(filter(lambda x:x%2==0,var))
print(ev)

#MAP is used for mathematical operation
#filter is used for conditional operation


var=[10,7,5,8,4,2,67,5,0,23.0,23.5]
sa=list(filter(lambda x:x**2,var))
print(sa)


print("#suming the whole list:-----------")


from functools import reduce
var=[10,7,5,8,4,2,67,5]
sa=reduce(lambda x,y:x+y,var)
print(sa)



