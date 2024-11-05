##print revrse 586 of 685___
print("prg 1")

##using slicing:
var= 586
a=str(var)
print(a[::-1])


##using while loop: wrong program
print("prg 2")


var=[4,5,6]
i=1
for  i in range(len(var)):
    i=-i
    
    print(var[i])
    i=+1
    




print("prg 3")
a=2
while(a<10):
    a=a+2
    print(a)

    
##Var="India"
##for x in Var:
##    while(x<"d"):
##        print(x)
#### Result --> it will print as "d" continously (condition satisfied and print as infinite). Hence, we should not give for and while at same time by giving ==
##
##var=[4,5,6]
##for  i in var[:-1]:
##    print(var)




print("+++++++++++++++++while loop from cs50+++++++++++++++")


print("hello world")

print("meow")
print("meow")
print("meow")

# i = 3
# while i != 0:
#     print("meow")


i = 3
while i != 0:
  print("meow")
  i = i - 1

  i = 1
  while i <= 3:
      print("meow")
      i = i + 1
      
i=0
while i <3 :
    print("mmamama")
    i=i+1

for _ in range(3):
    print("meow")
    
print("meow\n" * 3, end="")



while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break
    
def main():
    meow(get_number())


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("meow")


main()