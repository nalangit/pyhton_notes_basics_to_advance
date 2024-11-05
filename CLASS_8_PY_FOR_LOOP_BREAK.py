var="india"
for x in var:
     print(x)
print("____________________nextpg_____________________")
var ="samsung"
for x in var:
    print(x)




print("____________________nextpg_____________________")

var =["dhoni","azar","yusuf",7]
for x in var:
    print(x)

print("____________________nextpg_____________________")

var="india"
for x in var[2]:
  print(x)
   
print("____________________nextpg_____________________")

var="india"
for x in var:
    if(x =='d'):
        print(x)
    
    print("____________________nextpg_____________________")




# In[1]:
## method to get the particular element in string using for loop


var="samsung"
for x in var:
    if(x=="s"):
        print(x)
    
    
print("____________________nextpg_____________________")



# In[10]:
##to get the small "s"from samsung

var="Samsung"
var.lower()   ##converting the string to lower case
for x in var:
    
    if(x=='s'):
        print(x)
    

print("____________________nextpg_____________________")


##BREAK

var="ganguly"
for x in var:
    if(x=="g"):
      print('present')
    elif (x!="g"):
      print("not present")
      ##o/p:present
       ##present

      ## there will be two present because "g "occurs two times in ganguly so iteration is completed for all strings


        
var = "gangulyl"
for x in var:
    match x:
        case "g" | "l":
            print("present")
        case _:
            print("not present")
print("____________________nextpg_____________________")

##using break statement:


var="ganguly"

for x in var:
   
    if(x=="g"):
    
        print("present")
        break
     #o/p:present

     ## there will be only one present in output because the iteration is stoped after finding first "g"in the string :ganguly....break statement breaked the iteration and exited the if conditon
     
print("____________________nextpg_____________________")



# In[22]:
## if and else


var="rahul"
for x in var:
    if(x=="a"):
        print("avail")
    else:
        print("unavail")
        
    
print("____________________nextpg_____________________")

    


# In[23]:


var=["dhoni","yuvi","jaddu","kohli"]
for x in var:
    if(x=="yuvi"):
        print("present")
    else:
        print("not present")
        
print("____________________nextpg_____________________")


