#---------------    ERROR AND EXCEPTION HANDLING

##var=10/0
##print(var)
##
##output::
##  var=10/0
##ZeroDivisionError: division by zero

try :
     var=10/0
     print(var)

except:
    print('bad')

print('nxt prg--------2')


##for zero division error alone print bad:

try :
     var=10/0
     print(var)

except(ZeroDivisionError):
         print('bad')

print('nxt prg--------3')



#printing a non string::
##
##try :
##     var=dhoni
##     print(var)
##
##except(ZeroDivisionError):
##         print('bad')
##output## var=dhoni
##NameError: name 'dhoni' is not defined

print('nxt prg--------4')
try :
     var=dhoni
     print(var)

except(ZeroDivisionError):
         print('bad')
except:
     print('good')

####o?p::::good



print('nxt prg--------5')
try :
     var=10+'a'
     print(var)

except(ZeroDivisionError):
         print('bad')
except(NameError):
     print('good')
except:
    print('heloo')


print('nxt prg--------6')
##it is a type error::
try :
     var=10+'a'
     print(var)

except(ZeroDivisionError,NameError):
         print('bad')

except:
    print('heloo')



print('nxt prg--------7')
try :
     var=10
     print(var)

except(ZeroDivisionError,NameError):
         print('bad')

except:
    print('heloo')


print('nxt prg--------8')
##else in exceptional handling
try :
     var=10
     print(var)

except(ZeroDivisionError,NameError):
         print('bad')

except:
    print('heloo')

else:
    print("else part")

##o/p
####heloo
####10
####else part


print('nxt prg--------9')
##finaly in exceptional handling........finaly is used to print the final statement wether it satisfies the try condition or not
try :
     var=10
     print(var)

except(ZeroDivisionError,NameError):
         print('bad')

except:
    print('heloo')

else:
    print("else part")
finally:
    print('this is final')

##10
##else part
##this is final
print('nxt prg--------10')
##finaly in exceptional handling
try :
     var=10/0
     print(var)

except(ZeroDivisionError,NameError):
         print('bad')

except:
    print('heloo')

else:
    print("else part")
finally:
    print('this is final')
    
print('nxt prg--------11')

## these folllowing steps are not useable for higher purpose because we dont know what error will come,,, nxt part is for those kinda thing ::
    ## to print the exact err0r as oupuy::
try :
    var=10/0
    print(var)
except ZeroDivisionError as a:
    print(a)
##division by zero


print('nxt prg--------12')


##    ## to print the exact err0r as oupuy::
##try :
##    var=10+'a'
##    print(var)
##except ZeroDivisionError as a:
##    print(a)
##
####o/:
##     var=10+'a'
##TypeError: unsupported operand type(s) for +: 'int' and 'str'
##
##
##
print('nxt prg--------13')


    ## to print the exact err0r as oupuy::
try :
    var=10+'a'
    print(var)
except TypeError as a:
    print(a)


##o/p:
####unsupported operand type(s) for +: 'int' and 'str'

print('nxt prg--------14 ')


   ## to print the exact  what ever err0r as oupuy::
##try :
##    var=10+'a'
##    print(var)
##except  Error as a:
##    print(a)

    
##except as  a not understand by python::
print('nxt prg--------15')


   ## to print the exact  what ever err0r as oupuy::
try :
    var=10+'a'
    print(var)
except  Exception as a:
    print(a)
#unsupported operand type(s) for +: 'int' and 'str'


print('nxt prg--------16')
try:
    def fun(a,b):
     print(a+b)
    fun()
except Exception as a:    
      print(a)
    

##o/pfun() missing 2 required positional arguments: 'a' and 'b'


