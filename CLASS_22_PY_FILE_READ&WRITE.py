#write-read


##var = open('sample.txt',"w+")
##var.write("tech")
##var.seek(0)
##a= var.read()
##print(a)
##
##
####read-write
##var=open("sample.txt","r+")
##a=var.read()
##print(a)
##var.write("alll arre")
##var.close()


var=open("sample.txt","r")
print(var.read())

var=open("sample.txt","r")
print(var.readline())

var=open("sample.txt","r")
print(var.read(2))


#readlines
var=open("sample.txt","r")
print(var.readlines())


print("=====================nxttype=======================")


with open("text.txt","w")as var:
    var.write("hello")



with open("text.txt","r")as var:
    a=var.read()
    print(a)

    

print("=====================nxttype=======================")


with open("text.txt","a")as var:
  var.write("\ mornig bonjour")
 ##recode

print("=====================nxttype=======================") 

#write+read
with open("text.txt","w+") as var:
    var.write("\nnormal")
    var.seek(0)
    a=var.read()
    print(a)
print("=====================nxttype=======================") 
# read+ write
with open("text.txt","r+")as var:
    print(var.read())
    var.write("zooommmmm")


print("=====================nxttype=======================")


## to write a list of name one by one in next line:
var=["dhoni","kholi","kallis","mccullum"]
for x in var:
    a=open("best.txt","a+")
    b=a.read()
    length=len(b)
    if (length>0):
        a.write("\n")
        a.write(x)
        a.close()
    else:
        a.write(x)
        a.write("\n")
        a.close()
print(.read())
        
