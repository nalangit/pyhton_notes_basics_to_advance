from datetime import *

var=datetime.now()
print(var)

var1=var.replace(microsecond=0)
print(var1)

var2=var1+timedelta(minutes=60)
print(var2)


var2=var2+timedelta(minutes=10)
print(var2)


var2=var2-timedelta(minutes=10)
print(var2)

#to arrange date time in a format

fmt="%d/%m/%y %H-%M-%S"
var4=datetime.strftime(var2,fmt)
print(var4)
