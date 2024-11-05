##class 9 apr 25

##ELIF : prevent morethan one condition from var

var ="india"
for x in var:
    if (x=="d"):
        print("success")
    elif(x=="n"):
            print('good')
    else:
       print ('not good')



print("##break nxt p")





var ='aaabbccccdde'
for x in var:
    if(x=='aaa','bb','cccc','dd','e'):
      print('abcde')
      break




var ='aaabbccccdde'
for x in var:
    if(x=='aaa'):
      print('abcde')
      break
print("##break nxt p")

## for geting abcde we can use three ways


print(' to convert it to set')
var ='aaabbccccdde'
a=set(var)
print (a)


print(' to convert it to list')

b=list(a)
b.sort()
print(b)
new=""
for x in b:
    new=new+x
    print(x)

    
print("##break nxt p 2nd condition")


##2nd condition(doubt)
var ='aaabbccccdde'
new=''
for x in var:
    if x in new:
        pass
    else:
        new=new+x
print(new)

print("##break nxt p 3rd condition")


var ='aaabbccccdde'
new=''
for x in var:
    if x not in new:
        new=new+x
print(new)

pritn("break")
## elif

Var=["dhoni","Kholi","yuvi","jaddu"]
for x in Var:
    if(x=="Kholi"):
        print("RCB")
    elif(x=="dhoni"):
        print("CSK")
    else:
        print("India")      







