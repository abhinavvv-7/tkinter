from tkinter import *
from tkinter.scrolledtext import ScrolledText as st
    
root = Tk()
tfn = StringVar() 
tln = StringVar()
ostr = StringVar()
def read_entries():
    fn = tfn.get()
    ln = tln.get()
    if (fn and ln):
        t1.insert(END,' '.join([fn, ln])+'\n')
    tfn.set('')
    tln.set('')

l1 = Label(root, text="First Name")
l1.grid(row=0, column=0)
e1 = Entry(root, textvariable=tfn)
e1.grid(row=0, column=1)

l1 = Label(root, text="Last Name")
l1.grid(row=1, column=0)
e1 = Entry(root, textvariable=tln)
e1.grid(row=1, column=1)

b1 = Button(root, text="Input", command=read_entries)
b1.grid(row=0, column=2, rowspan=2, sticky=N+S+W+E)

t1 = st(root, width=30, height=10)
t1.grid(row=2, column=0, columnspan=3, sticky=W+E)
mainloop()