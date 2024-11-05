#------------------------------------REGULAR EXPRESSIONS---------6.6.2022---------------------------------------

print("------------------------------------------1")

##import re
##var ="india is my country"
##var1= re.match("india",var)
##print(var1)


##<re.Match object; span=(0, 5), match='india'>

#.group() is used to get the in  string or get output in formats except object

print("------------------------------------------2")

import re
var ="india is my country"
var1= re.match("india",var)
print(var1.group())


#india

##import re
##var ="india is my country"
##var1= re.match("INDIA",var)
##print(var1.group())

## print(var1.group())
##AttributeError: 'NoneType' object has no attribute 'group'

import re
var ="india is my country"
var1= re.match("INDIA",var,re.I)
print(var1.group())

#india



print("------------------------------------------3")
##import re
##var ="india is my country"
##var1= re.match("my",var)
##print(var1.group())
##
##print(var1.group())
##AttributeError: 'NoneType' object has no attribute 'group'
##


print("------------------------------------------4")

import re
var ="india is my country"
var1= re.match("india is my",var)
print(var1.group())



print("------------------------------------------5")

#.match() will match from the begining of the string

#search:

import re
var ="india is my country"
var1= re.search(" my",var)
print(var1.group())


print("------------------------------------------6")

import re
var ="<html><head><html>"
var1= re.match("<.*>",var)
print(var1.group())



print("------------------------------------------7")


#?............is acts just like break
import re
var ="<html><head><html>"
var1= re.match("<.*?>",var)
print(var1.group())



print("------------------------------------------8")



import re
var ="india is smarterthan china"
var1= re.search(".* is .*",var)
print(var1.group())




print("------------------------------------------9")



import re
var ="india is smarterthan china"
var1= re.search("(.*) is (.*)",var)
print(var1.group(1))
print(var1.group(2))



print("------------------------------------------10")



import re
var ="india is smarter than china"
var1= re.search("(.*) is (.*) (.*)",var)
print(var1.group(1))
print(var1.group(2))
print(var1.group(3))



print("------------------------------------------11")




import re
var ="india is smarter than china"
var1= re.search("(.*) is (.*?) (.*)",var)
print(var1.group(1))
print(var1.group(2))
print(var1.group(3))



print("------------------------------------------12")


import re
var ="india is my country"
var1= re.search(".*",var)
print(var1.group())

print("------------------------------------------13")

import re
var="98765"
var1=re.sub("6","7",var)
print(var1)
var2=re.sub("5","10",var1)
print(var2)

print("------------------------------------------14")
#var=re.compile("[a-z]")-------matches only the first letter

import re
var=re.compile("[a-z]")
var1=var.match("india")
print(var1.group())



print("------------------------------------------15")
#var=re.compile("[a-z]+") -----+ matches all string


import re
var=re.compile("[a-z]+")
var1=var.match("india")
print(var1.group())


import re
var=re.compile("[A-Z]+")
var1=var.match("INDIA")
print(var1.group())

##------------------------------------------14
##i
##------------------------------------------15
##india


print("------------------------------------------15")

import re
var=re.compile("[0-9]")
var1=var.match("87568")
print(var1.group())


print("------------------------------------------15")


import re
var=re.compile("[0-9]+")
var1=var.match("87568")
print(var1.group())


print("------------------------------------------15")


import re
var=re.compile("[0-9]")
var1=var.match("87568")
print(var1.group())

print("------------------------------------------15")

import re
var="india scored 350 runs in 30 overs with 9 extras"
var1=re.findall("\w",var)
print(var1)

print("-------------------------------------------------------15")
#caps-W

import re
var="india scored 350 runs in 30 overs with 9 extras"
var1=re.findall("\W",var)
print(var1)

print("------------------------------------------15")

import re
var="india scored 350 runs in 30 overs with 9 extras"
var1=re.findall("\d",var)
print(var1)

print("------------------------------------------15")

import re
var="india scored 350 runs in 30 overs with 9 extras"
var1=re.findall("\D",var)
print(var1)

print("------------------------------------------15")

import re
var="india scored 350 runs in 30 overs with 9 extras"
var1=re.findall("\s",var)
print(var1)

print("------------------------------------------15")

import re
var="india scored 350 runs in 30 overs with 9 extras"
var1=re.findall("\S",var)
print(var1)


##\w--------- matches alphabets+numbers without space
##\W--------- space
##\d---------numbers
##\D---------alphabets+space
##\s----------space
##\S----------alphabets+numbers without spaces

print("------------------------------------------15")

#{3}------represents 3 digit num
import re
var="india scored 350 runs in 30 overs with 9 extras"
var1=re.findall("\d{3}",var)
print(var1)

print("------------------------------------------15")

import re
var="india scored 350 runs in 30 overs with 9 extras"
var1=re.findall("\d{1,3}",var)
print(var1)

print("------------------------------------------15")

import re
var="india scored 350 runs in 30 overs with 9 extras"
var1=re.findall("\d{1,2}",var)
print(var1)


print("------------------------------------------------15")
# balamurugan1990@gmail.com--valid
# surya 1992 @gamil.com ---valid
# nala@gamil.com-----------invalid

import re
var=str(input("enter e mail:"))
condition ="[a-z]+[0-9]+[@]\D{5}[.]\D{2,3}"


if(re.search(condition,var)) :
    print("valid")
else:
    print("invalid")
