from tkinter import *
from tkinter import ttk
from tkinter .ttk import *
from tkinter import messagebox
from tkinter import Menu

window =Tk()
window.title("welcome")
window.geometry('350x250')

menu=Menu(window)
new_item=Menu(menu)
new_item.add_command(label = 'New')
new_item.add_separator()
new_item.add_command(label='Edit')
new_item.add_separator()
new_item.add_command(label='Save')
menu.add_cascade(label ='File',menu=new_item)
window.config(menu=menu)

window.title("first")
a= Label(window,text = "username").grid(row =0,column =0)
b= Label(window,text= "password").grid(row=1,column=0)
e= Entry(window).grid(row=0,column =1)
f= Entry(window,show="*").grid(row =1,column =1)
def clicked():
     messagebox.showinfo('Login sucsess','Login sucess')
c= ttk.Button(window,text="Login",command = clicked).grid(row=10,column=0)
h= ttk.Button(window,text ="quit",command = window.destroy).grid(row =10,column =1)
g= Label(window,text ="programing lang.").grid(row =2,column =0)


rad0=Label(window,text="Gender").grid(row=4,column=0)
rad1= Radiobutton(window,text="woman",value=1).grid(row =6,column =0)
rad2= Radiobutton(window,text="man",value=2).grid(row=7,column =0)

combo =Combobox(window)
combo['value']=('phyton','c++','c','c#','java','js')
combo.current(0)
combo.grid(row = 2,column =1)
window.mainloop()