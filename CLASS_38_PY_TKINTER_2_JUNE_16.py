

#file path operations: to create new files and messages:

##
##import tkinter
##from tkinter import filedialog
##
##root=tkinter.Tk()
##var=tkinter.filedialog.askdirectory()
##filename="new1_txt"
##path=var+"/"+filename
##var1=open(path,"w")
##var1.write("besant")
##var1.close()


 
import tkinter
from tkinter import filedialog
import os
from tkinter import messagebox

root=tkinter.Tk()
root.withdraw()

var=tkinter.filedialog.askdirectory()
filename="fri_june_17_txt"
path=os.path.join(var,filename)
var1= open(path,"w")
var1.write("school")
var1.close()
messagebox.showinfo("besant",path)
