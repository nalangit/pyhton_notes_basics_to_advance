
##class  12 range

##to print 0 to 9
for x in range(10):
    print(x)
print("nxt prg")
#a=int(input("enter 1st int:"))
#b=int(input("enter 2nd  int:"))
#c=int(input("enter 3rd int:"))
#d=[]
#d.append(a)
#d.append(b)
#d.append(c) ## append or d.extend[a,b,c]
#print(d)
#for x in d:
#    for y in d:
#        for z in d:
#            if(d[x]!=d[y] and d[y]!=d[z] and d[z]!=d[x]):
#             print(d[x],d[y],d[z])


             
##to print 0 to 9
for x in range(0,10):
    print(x)
    
print("nxt prg")


for x in range(2,10):
    print (x)

print("nxt prg")
for x in range(0,10,2):
               
  print(x)



print("nxt prg")
for x in range(10,0,-2):
    print(x)
print("nxt prg")


a=int(input("enter 1st int:"))
b=int(input("enter 2nd  int:"))
c=int(input("enter 3rd int:"))
d=[]
d.append(a)
d.append(b)
d.append(c) ## append or d.extend([a,b,c])
print(d)
for x in range(3):
    for y in  range(3):
        for z in range(3):
            if(d[x]!=d[y] and d[y]!=d[z] and d[z]!=d[x]):
             print(d[x],d[y],d[z])
print("nxt prg")

a=int(input("enter 1st int:"))
b=int(input("enter 2nd  int:"))
c=int(input("enter 3rd int:"))
d=[]
d.extend([a,b,c]) ## append or d.extend([a,b,c])
print(d)
for x in range(3):
    for y in  range(3):
        for z in range(3):
            if(d[x]!=d[y] and d[y]!=d[z] and d[z]!=d[x]):
             print(d[x],d[y],d[z])

#ent a:4
#ent b:5
#ent c:6
#[4, 5, 6]
#4 5 6
#4 6 5
#5 4 6
#5 6 4
#6 4 5
#6 5 4

print("next prg")

a= []
for x in range(0,3):
 for y in range(0,3):
   for z in range(0,3):
       a.append([x,y,z])
print(a)


##o/p:::::[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [0, 2, 0], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]

