###tkinter_1-------------
###it has two things they are components(buttons) and  events(buttons actions)
##
from tkinter import*
import sqlite3
root=Tk()
root.title("my box")
root.geometry("600x400")


name_entry=StringVar()
age_entry=StringVar()
gender_entry=StringVar()

#submit button code
def submit():
    connection=sqlite3.connect("TKINTER_JUNE_17.db")
    cursor=connection.cursor()
    cursor.execute("insert into customer values(:name,:age,:gender)",
     {
      'name':name_entry.get(),
      'age':age_entry.get(),
      'gender':gender_entry.get()
      }
    )
    name_entry.delete(0,END)
    age_entry.delete(0,END)
    gender_entry.delete(0,END)
    
    connection.commit()
    connection.close()

###########################################################
#SHOW BUTTON CODE:----------------JUNE_20

from tkinter import messagebox
def show():
    conn=sqlite3.connect("TKINTER_JUNE_17.db")
    cursor=conn.cursor()
    cursor.execute('select * from customer where name=? AND age=? AND gender=?',(name_entry.get(),age_entry.get(),gender_entry.get()))
    data=cursor.fetchone()
    if data:
        messagebox.showinfo('message',"user already exsists")
    else:
        messagebox.showinfo('message','no user present')
    conn.commit()
    conn.close()


name=Label(root,text="NAME")
name.grid(row=0,column=0)
name_entry=Entry(root,width=30)
name_entry.grid(row=0,column=1)

age=Label(root,text="AGE")
age.grid(row=1,column=0)
age_entry=Entry(root,width=17)
age_entry.grid(row=1,column=1)


gender=Label(root,text="gender")
gender.grid(row=2,column=0)
gender_entry=Entry(root,width=25)
gender_entry.grid(row=2,column=1)

submit=Button(root,text="submit",command=submit)
submit.grid(row=3,column=0)
show=Button(root,text="show",command=show)
show.grid(row=3,column=1)
cancel=Button(root,text="cancel",command=root.destroy)
cancel.grid(row=3,column=2)


### data base code for sqlite3 for creating a table:-----we have  to command this code after running it for 1 time


##import sqlite3
##connection =sqlite3.connect ("TKINTER_JUNE_17.db")
##cursor=connection.cursor()
##query=cursor.execute("create table customer(name text,age int,gender text)")
##connection.commit()
##connection.close()

