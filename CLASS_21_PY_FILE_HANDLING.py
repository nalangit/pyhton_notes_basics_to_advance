var=open("sample.txt","w")
var.write("hello")
var.close()


var=open("new.txt","w")
var.write("--------NALAN--------")
var.close()

var=open("sample.txt","w")
var.write("hiiiiiiii")
var.close()


##if we use 'w' it will overwrite in the same things
##to get one by one use "a" append

var=open("sample.txt",'a')
var.write("heggfbjdxhfdzdfgaidsllo")
var.close()
## to read the written file:
var=open("sample.txt",'r')
a=var.read()
print(avar=open("sample.txt","w")

var.write("hello")
var.close()
[4]
var=open("new.txt","w")
var.write("hi this is soorya")
var.close()
[34]
var=open("sample.txt","w")
var.write("hi")
var.close()
[32]
var=open("sample.txt","a")
var.write("  hello")
var.close()
[35]
var=open("sample.txt","r")
a=var.read()
print(a)
hi

[2]
var=open("sample.txt","w+")
var.write("besant")
a=var.read()
print(a)


[8]
var=open("sample.txt","w+")
var.write("tech")
var.seek(0)
a=var.read()
print(a)
tech

seek moves the cursor to desired place.

[9]
var=open("sample.txt","r+")
a=var.read()
print(a)
var.write("best")
var.close()
tech

[10]
var=open("sample.txt","r")
print(var.read())
dhoni
kohli
rohit
hardik
bumrah

[17]
var=open("sample.txt","r")
print(var.readline())
dhoni


[18]
var=open("sample.txt","r")
print(var.readlines())
['dhoni\n', 'kohli\n', 'rohit\n', 'hardik\n', 'bumrah']

[37]
with open("next.txt","w") as var:
    var.write("hi i am chitti, the robot.")
    
[38]
with open("next.txt","a") as var:
    var.write("\nspeed one terra hert, memory one zeta byte")
[39]
with open("next.txt","r") as var:
    a=var.read()
    print(a)
hi i am chitti, the robot.
speed one terra hert, memory one zeta byte

[40]
with open("next.txt","w+") as var:
    var.write("upgraded,")
    var.seek(0)
    print(var.read())
upgraded,

[41]
with open("next.txt","r+") as var:
    print(var.read())
    var.write("\nversion 2.0")
upgraded,

[42]
with open("next.txt","r") as var:
    print(var.readline())
upgraded,


[43]
with open("next.txt","r") as var:
    print(var.readlines())
['upgraded,\n', ' version 2.0']

