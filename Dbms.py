from tkinter import *
from customtkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import os

root = CTk()
root.geometry("1280x800")
root.title("Fine management system")
image1 = Image.open('C://Users//Sanath S//Desktop//Web Dev//python//lock.jpg')
resized1 = image1.resize((15,15))
lockimage = ImageTk.PhotoImage(resized1)
locklabel = Label(root,image =lockimage )
locklabel.place(x=775,y=520)

image2 = Image.open('C://Users//Sanath S//Desktop//Web Dev//python//logo.png')
resized2 = image2.resize((15,15))
useimage = ImageTk.PhotoImage(resized2)
uselabel = Label(root,image =useimage )
uselabel.place(x=775,y=420)

image3 = Image.open('C://Users//Sanath S//Desktop//Web Dev//python//home.jpg')
resized3 = image3.resize((70,70))
logoimage = ImageTk.PhotoImage(resized3)
logolabel = Label(root,image =logoimage,bg='black')
logolabel.place(x=900,y=320)

usernamelabel = CTkLabel(root,text="Username")
usernamelabel.place(x=560,y=330)
username = CTkEntry(root,width=250)
#username.insert(END,'Enter username')
username.place(x=645,y=330)

pwdlabel = CTkLabel(root,text="Password")
pwdlabel.place(x=560,y=410)
pwd = CTkEntry(root,width=250)
pwd.configure(show="*")
pwd.place(x=645,y=410)
def log():
    if username.get() in ['Sanath'] and pwd.get() in ['san']:
        confirm = messagebox.askyesno("Confirm","Are u sure")
        if confirm==True:
            new = CTkToplevel()
            #root.destroy()
            new.title("Fine management system")
            new.geometry("600x400")

        else:
            pass
    else:
        confirm = messagebox.showerror("Error","Wrong Password try again")
        username.delete(0,END)
        pwd.delete(0,END)
login = CTkButton(root,text='Login',command=lambda:log())
login.place(x=680,y=500)



root.mainloop()