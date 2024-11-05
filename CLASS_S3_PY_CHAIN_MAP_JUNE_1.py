#--------------------------------CHAIN MAP--------------------

from collections import ChainMap
var=[10,7,2,3]
var1=[2,4,5,6,7]
a=ChainMap(var,var1)
print(a)



print("--------------------------------------------2")


from collections import ChainMap
a={"name":"don","age":67}
b={"name":"booon","age":87657}
d=ChainMap(a,b)
print(d)

print("--------------------------------------------3")

from collections import ChainMap
f="dhoni"
g=[1,3,5,67]
i=ChainMap(f,g)
print(i)

print("--------------------------------------------4")

from collections import ChainMap
f="dhoni"
g=[1,3,5,67]
i=ChainMap[f,g]
print(i)

print("--------------------------------------------5")


#--------------------------------------counter--------------------

from collections import Counter
var="india is my country"
b=Counter(var)
print(b)


#Counter({'i': 3, ' ': 3, 'n': 2, 'y': 2, 'd': 1, 'a': 1, 's': 1, 'm': 1, 'c': 1, 'o': 1, 'u': 1, 't': 1, 'r': 1})
  #counter is used to arrange the elements in dict format and it also shows how many times the element is repeated

print("-----------------------------------6")

#------------------------ORDERED DICT-------------------------

#normal dict
a={}
a[1]="dhoni"
a[2]="kholi"
a[3]="yuvi"
print(a)


print(a[2])


a.pop(2)
print(a)

a[2]="samsung"
print(a)


##{1: 'dhoni', 2: 'kholi', 3: 'yuvi'}

##kholi

##{1: 'dhoni', 3: 'yuvi'}

##{1: 'dhoni', 3: 'yuvi', 2: 'samsung'}



#print(a[5])
##print(a[5])
##KeyError: 5
##

print("-----------------------------------------------7")


#ordered dict:

from collections import OrderedDict
a=OrderedDict()
a[1]="dhoni"
a[2]="kholi"
a[3]="yuvi"


print(a)
#OrderedDict([(1, 'dhoni'), (2, 'kholi'), (3, 'yuvi')])

print(a[2])
#kholi

a.pop(2)
print(a)
#OrderedDict([(1, 'dhoni'), (3, 'yuvi')])

a[2]="samsung"
print(a)

#OrderedDict([(1, 'dhoni'), (3, 'yuvi'), (2, 'samsung')])

a[4]="gangu"
print(a)

#OrderedDict([(1, 'dhoni'), (3, 'yuvi'), (2, 'samsung'), (4, 'gangu')])



##print(a[5])
## print(a[5])
##KeyError: 5
# TO OVERCOME THIS ERROR WE HAVE DEFAULT DICT:

##DEAFULY DICT::

from collections import defaultdict
def fun():

    return "nokey"
a=defaultdict(fun)
a[1]="dhoni"
a[2]="kholi"
a[3]="raina"
print(a)


#defaultdict(<function fun at 0x000001559BDB8940>, {1: 'dhoni', 2: 'kholi', 3: 'raina'}


print(a[4])
#nokey

#if the particular key is not found it will return the function output
