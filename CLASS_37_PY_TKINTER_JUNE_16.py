#tkinter_1-------------
#it has two things they are components(buttons) and  events(buttons actions)

from tkinter import*
root=Tk()
root.title("my box")
root.geometry("600x400")
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

submit=Button(root,text="submit")
submit.grid(row=3,column=0)
show=Button(root,text="show")
show.grid(row=3,column=1)
cancel=Button(root,text="cancel",command=root.destroy)
cancel.grid(row=3,column=2)


