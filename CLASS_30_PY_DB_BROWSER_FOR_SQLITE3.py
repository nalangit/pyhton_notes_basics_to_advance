#--------------------------------------------------SQLITE3--------------------------------------



##import sqlite3
##
##connection =sqlite3.connect("sample.db")
##cursor=connection.cursor()
##query= cursor.execute("create table beasnt(name text  ,age int)")
##connection.commit()
##connection.close()
##
##
##
###insert query
##
##import sqlite3
##
##connection =sqlite3.connect("sample.db")
##cursor=connection.cursor()
##query= cursor.execute("insert into beasnt(name  ,age ) values('dhoni',40)")
##connection.commit()
##connection.close()
##
##
###insert  query for multiple values:
##
##import sqlite3
##
##connection =sqlite3.connect("sample.db")
##cursor=connection.cursor()
##query= cursor.execute("insert into beasnt(name  ,age ) values('dhoni',40) ,('yuvi',50),('rai',67),(99,'don')")
##connection.commit()
##connection.close()


# to fetch the data from DB:
##
##import sqlite3
##
##connection =sqlite3.connect("sample.db")
##cursor=connection.cursor()
##query= cursor.execute("select * from beasnt")
##data=cursor.fetchall()
##print(data)
##connection.commit()
##connection.close()
##
###------------------------------------------
## #to import  whose age is equal to 40:
##import sqlite3
##
##connection =sqlite3.connect("sample.db")
##cursor=connection.cursor()
##query= cursor.execute("select name from beasnt where age=40")
##data=cursor.fetchall()
##print(data)
##connection.commit()
##connection.close()
##
##
##import sqlite3
##
##connection =sqlite3.connect("sample.db")
##cursor=connection.cursor()
##query= cursor.execute("select name from beasnt where age>=47")
##data=cursor.fetchall()
##print(data)
##connection.commit()
##connection.close()
##
##
### updating or modifying data:
##
##
##import sqlite3
##
##connection =sqlite3.connect("sample.db")
##cursor=connection.cursor()
##query= cursor.execute("update beasnt set age=42 where name='dhoni'")
##
##connection.commit()
##connection.close()

# deleting data
##
##import sqlite3
##
##connection =sqlite3.connect("sample.db")
##cursor=connection.cursor()
##query= cursor.execute("delete  from beasnt where age=42 ")
##
##connection.commit()
##connection.close()



### creating a table with id ,product,company
##import sqlite3
##
##connection =sqlite3.connect("ELE TECH.db")
##cursor=connection.cursor()
##query= cursor.execute("create table elec(id int ,product text , company text)")
##connection.commit()
##connection.close()

##import sqlite3
##
##connection =sqlite3.connect("ELE TECH.db")
##cursor=connection.cursor()
##query= cursor.execute("insert into elec(id, product ,company)values(001,' charger' , 'philips'), (002,'mobile','moto'),(003,'sim','vi'),(004,'sd card','sandisk')")
##connection.commit()
##connection.close()


#----------------------------renaming the table
##import sqlite3
##
##connection =sqlite3.connect("sample.db")
##cursor=connection.cursor()
##query= cursor.execute("alter table beasnt rename to good")
##connection.commit()
##connection.close()

import sqlite3

connection =sqlite3.connect("sample.db")
cursor=connection.cursor()
query= cursor.execute("alter table good add column amount")
connection.commit()
connection.close()

