                                                             ## CLASS 1 06.04.2022.................. BASICS.......


##var = india
##print(var)

var = "india"
print(var)
print(type(var))

var = 'india'
print(var)
print(type(var))

var =''' india'''
print(var)
print(type(var))

var = 10
print(var)
print(type(var))

var = "10"
print(var)
print(type(var))

##any number or variable declared inside quotes are consider as string

var =10.5
print(var)
print(type(var))

var1 =10
var2 =20
print(var1+var2)

var1 ="10"
var2 ="20"
print(var1+var2)
## string concatenation o|p =1020

var1 = 10
var2 =5.5
print(type(var1 +var2))
##the process of converting one data type to another data type is called "TYPECASTING"(implicit typecasting)
##eg o\p 10.5 (int +float becomes float)
## there are two types of type casting
## 1.implicit typecasting
## 2.explicit typecasting

##var1 = "dhoni"
##var2 = 7
##print(type(var1 +var2))

## a str and int cannot be added
## reason : int is numerical datatype and str is sequential datatype (EXPLICIT TYPECASTING)

var1 = "dhoni"
var2 = 7
print(var1 + str(var2))
## a string cannot be converted to int ,but a INT can be converted to STR





                                                             ##PRINT STATEMENT
## type 1

var = "dhoni"
print (var,"is my captain")

## dhoni and kholi are best frnds
var1= "dhoni"
var2 = "kholi"
print( var1,"and",var2,"are best frnds")

##type 2
var1 ="dhoni"
var2 =" kholi"
print("%s and %s are best frnds" %(var1,var2)) ## var 1 will be allocated for 1st %S and var2 will be allocated 2nd %s

## %s ...... string
## %d...... int
## %f........float
a =10
print(10)


                                          ##................. ##PRINT STATEMENT TYPE 3  [07.04.2022] CLASS2

var1 ="dhoni"
var2 =100
print("{} scored {} runs".format(var1,var2)) 
print("{} scored {} runs IN THE LAST MATCH".format(var1,var2))

##PRINT STATEMENT EXAMPLE

##INDIA score 350 runs against SRILANKA in 39 over with 9 extras

##type1
var1= "india"
var2 =350
var3 ="srilanka"
var4 =39
var5=9
print(var1,"score",str(var2),"runs against ",var3,"in",str(var4),"overs with",str(9),"extras")

##type2

var1= "india"
var2 =350
var3 ="srilanka"
var4 =39
var5=9
print("%s score %s runs against %s in %s overs with %s extras"%(var1,var2,var3,var4,var5))

##type 3
var1= "india"
var2 =350
var3 ="srilanka"
var4 =39
var5=9
print("{} score {} runs against {} in {} overs with {} extras".format(var1,var2,var3,var4,var5))

