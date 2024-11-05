


                               #### STRING SLICING CLASS......2............. 07.04.22

var ="india"
print(var[2])



var ="samsung" ##..................................print m and u in samsung
print(var[2])
print(var [4])

var="samsung"
print(var[2],var[4])

var ="ms dhoni"
print(var[4])

var ="india" ##...................negative indexing
print(var[-3])

## there are two type of indexing 1. positive indexing ,2. negative indexing.


var ="samsung" ##..................................print m and u in samsung using NEGATIVE INDEXING
print(var[-5])
print(var [-3])
print(var[1:4]) ##................................ syntax : print(variable_name[start : stop].............start = index value , stop = count value

var ="ganguly"
print(var[3:6]) ##............to print gul
print(var[2:5]) ##...............to print ngu
print(var[-4:-1]) ##....................to print gul







                             ##................................... CLASS .............3,,,,,,,,,,,, 08.04.22

##example:::
var ="srilanka"
print(var[3]) ##......l
print(var[-5]) ##....l
print(var[-1]) ##.....a
print(var[7]) ##....a
                                                                ##.................. to print in 4 different ways...............

print(var[3:6]) ##.............p-p.....idex :value
print(var[3:-2]) ##............p-n.....index:value of next digit
print(var[-5:-2]) ##...........n-n.....value:value of next
print(var[-5:6]) ##............n-p.....value: value

## to print LIR in reverse
print(var[-4:-7]) ##....reverse slicing is not possible in between the string but whole string can be reversed

var="srilanka"
print(var[::-1]) ###....... o\p aknalirs
print(var[::-2]) ##......anlr
print(var[::-3]) ##.....aar

                        ### syntax: print(variable_name[:: value])......not index

print(var[::1]) ##........srilanka
print(var[::2]) ##........siak
print(var[::3]) ##.........slk

var = 456
##print(var[1])   #####......its integer ....error: int object is not subscriptable.....
print((str(var)[1])) ## EXPLICIT TYPECASTING

var ="456"
print(var[1])

