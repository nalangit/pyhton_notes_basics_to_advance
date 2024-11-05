
       ##                       DICT COMPREHENSION--------MAY 23

##converting list to dict using COMPREHENSION

var=[10,7,9,33,8]
a={}
for x in var:
    a[x]=x
print(a)


var=[10,7,9,33]
z={ x:x for x in var}
print(z)

print("==========2222222222===============")
##to print power as value:::

var=[10,7,9,33]
a={}
for x in var:
    a[x]=x**2
print(a)


var=[10,7,9,33]
z={ x:x**2 for x in var}
print(z)


print("================3333333333333333======")
##to print even key value pairs:::::
var=[10,7,12,33]
a={}
for x in var:
    if (x%2==0):
        a[x]=x
print(a)

var=[10,12,17,44]
z={x:x for x in var if (x%2==0)}
print(z)


print("===================44444444444444==================")
var=["csk","mi","rcb"]
var1=["dhoni","polly","max"]
a={}
for x in var:
    for y in var1:
        a[x]=y
print(a)
##o/p::{'csk': 'max', 'mi': 'max', 'rcb': 'max'}____wrong ___method__ all values are same



var=["csk","mi","rcb"]
var1=["dhoni","polly","max"]
a=list(zip(var,var1))
print(a)
b={}
for x,y in a:
    b[x]=y
print(b)



z={x:y for x,y in zip(var,var1)}
print(z)


##zip:::::::zip is used to make a index based  tuple inside a list.....eg::(csk,dhoni) both are combined by index value 0

##OUTPUT:
##[('csk', 'dhoni'), ('mi', 'polly'), ('rcb', 'max')]=======PRINT(A)
##{'csk': 'dhoni', 'mi': 'polly', 'rcb': 'max'}================PRINT(B)
##{'csk': 'dhoni', 'mi': 'polly', 'rcb': 'max'}===============PRINT(Z)

