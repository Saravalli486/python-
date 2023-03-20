'''from tkinter import *
from tkinter import messagebox
t=Tk()
t.title("Welcome")
t.geometry("400x300")
Label(t,text="Username").grid(row=1,column=1)
Label(t,text="Password").grid(row=2,column=1)
a=Entry(t)
a.grid(row=1,column=2)
b=Entry(t,show="*")
b.grid(row=2,column=2)

def test():
    x=a.get()
    y=b.get()
    messagebox.showinfo(x,y)
    

Button(t,text="submit",command=test).grid(row=3,column=2)

t.mainloop()'''
from tkinter import * 
from tkinter import messagebox
window=Tk()
window.title('registration')
window.geometry("400x300")
Label(window,text="Username",bg='yellow',fg='blue',font='Corbel 12 italic').grid(row=1,column=1)
Label(window,text="Password").grid(row=2,column=1)
a=Entry(window)
a.grid(row=1,column=2)
b=Entry(window,show="*")
b.grid(row=2,column=2)
d={ }
def register():
    x=a.get()
    y=b.get()
    d[x]=y
    messagebox.showinfo(title='register',message='Registration successfully')
def signup():
    x=a.get()
    y=b.get()
    if x in d:
        if y== d[x]:
            print(y)
            messagebox.showinfo(title='signup',message='Signedup successfully')
        else:
            messagebox.showerror(title='signup',message='Password mismatch')
    else:
        messagebox.showerror(title='signup',message='Invalid user name')
        

Button(window,text="Register",command=register).grid(row=5,column=2)
Button(window,text="Signup",command=signup).grid(row=7,column=2)


            





    
    












