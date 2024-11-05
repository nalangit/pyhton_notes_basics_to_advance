##class 4  11.04.2022_____string manipulation

  ## dot attribute wil be working on only particular datatypes_______keyword means which is used in all datatypes

##var = "india intention india"
##print(var.count("in"))                      .........o/p 3

var = "india intention india"
print(var.count("in",3))                    #o/p: 2 ______starts from index value 3

var = "india intention india"
print(var.count("in",8,18))     ##...............o/p: 1 _______________starts from index value 8 and ends at value 18  


var = "india intention india"
print(var.find("in")) ##.....op/ 0


var = "india intention india"
print(var.find("in",3))      ##.....o/p  6

var = "india intention india"
print(var.find("in",8,20))    ##......o/p 16



var = "india intention india"
print(var.index("in"))    ##...o/p  0
print(var.index("in",3))  ##...o/p 6
print(var.index("in",8,20)) ##  ...o/p 16


##...DIFFERENCE BETWEEN .find AND .index


var ="westindies"
print(var.find("z"))  #.....o/p : -1  [index value will never be a negative value ]
##print(var.index("z")) #......o/p : error: substring not found



var = ("india is my country")
print(var.split("is"))
print(var.partition("is"))
###o/p
##['india ', ' my country']
##('india ', 'is', ' my country')


var = ("india is my country")
print(len(var))  ##.....len is a keyword ____ retuiurns lenth of the string starts from 1


var = ("!india is my country!")
print(var.strip("!"))  ## strip 


var = ("!india is my country!")
print(var.strip("is"))  ## strip cannot remove the word present in between the string


var = ("!india is my country!")
print(var.strip("!"))
print(var.lstrip("!"))
print(var.rstrip("!"))


var = ("india is my country")
print(var.upper())
print(var.lower())
print(var.title())
print(var.capitalize())


var = ("india is my country")
print(var.isupper())
print(var.islower())
print(var.istitle())


var = "india is my country"
print(var.startswith("india"))
print(var.endswith("country"))
print("is" in var)
 ###.................... STRING IS MUTABLE OR NOT MUTABLE............................................

var = "india"
print(var.replace("n","m"))##....ITS COPY OF THE MEMORY.....

var = "india"
var.replace("n","m") ### IN STRING WE CAN ABLE TO CHANGE ONLY THE COPY OF THE MEMORY....THE ORIGINAL MEMORY(variable- var )remains unchanged

print(var)




var = "india"
var=var.replace("n","m") 

print(var)






