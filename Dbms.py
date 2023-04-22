from tkinter import *
from customtkinter import*
from tkinter import ttk,font
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector as sqltor
import matplotlib
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.figure import Figure

root = CTk()
root.geometry("1280x800")
root.title("Fine management system")
global top2

#Link to database
mycon = sqltor.connect(host = "localhost", user = "root",passwd = "tiger",database = 'dbms')
if mycon.is_connected() == False:
    print("Database couldnt be connected")
cursor = mycon.cursor()

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
login = CTkButton(root,text='Login',command=lambda:log())
login.place(x=680,y=500)
def log():
    #if username.get() in ['Sanath'] and pwd.get() in ['san']:
        confirm = messagebox.askyesno("Confirm","Are u sure")
        if confirm==True:
            new1 = CTkToplevel()
            new1.attributes('-topmost', True)
            new1.title("Fine management system")
            new1.geometry("600x400")
            def create_frame():
                global frame1,frame2
                frame1 = CTkFrame(new1,height=830,width=240)
                frame1.place(x=0,y=0)
                frame2 = CTkFrame(new1,height=100,width=1265)
                frame2.place(x=260,y=0)

            frame3 = CTkFrame(new1,height=710,width=1100)
            frame3.place(x=260,y=120)
            my_font = CTkFont(family="<Futura>",size = 12)

            create_frame()
            Welcome = CTkButton(frame1,font=my_font,text = "Welcome Back\n"+username.get(),width=180,height=60)
            Welcome.place(x=20,y=25)

            Exp_button = CTkButton(frame2,text="Spend Analytics",width = 200,height = 35)
            Exp_button.place(x=500,y=25)
            
            def balance():
                
                top2 = CTkToplevel()
                top2.title(" ")
                new1.attributes('-topmost', False)
                top2.attributes('-topmost', True)
                top2.geometry("700x500")
                top2.resizable(False,False)
                top2.minsize(width=400,height=400)
                
                s = ttk.Style(top2)
                s.theme_use("clam")
                #cursor.execute('select * from student')

                tree = ttk.Treeview(top2)
                tree['show']='headings'
                tree['columns'] = ("User Id","Income","Type","Date","Account Id")
                tree.column('#0',width=0,minwidth=20)
                tree.column('User Id',width=120,minwidth=100)
                tree.column('Income',width=120,minwidth=100)
                tree.column('Type',width=120,minwidth=100)
                tree.column('Date',width=120,minwidth=100)
                tree.column('Account Id',width=120,minwidth=100)

                tree.heading('#0',text='',anchor=W)
                tree.heading('User Id',text='User Id',anchor=W)
                tree.heading('Income',text='Income',anchor=W)
                tree.heading('Type',text='Type',anchor=W)
                tree.heading('Date',text='Date',anchor=W)
                tree.heading('Account Id',text='Account Id',anchor=W)

                scroll = CTkScrollbar(top2,orientation="vertical")
                scroll.configure(command=tree.yview)
                tree.configure(yscrollcommand=scroll.set)
                scroll.pack(ipady=150,side = RIGHT)
                tree.place(x=70,y=100)
                tree.insert(parent='',index='end',iid=0,text='',values=(1,1000,'Credit','Tuesday',112390))
                tree.insert(parent='',index='end',iid=1,text='',values=(2,2000,'Debit','Wednesday',122490))
                def remove():
                    x = tree.selection()
                    for record in x:
                         tree.delete(record)
                    print(x)
                    
                delete_but = CTkButton(top2,text = "Delete",command = remove)
                delete_but.place(x=545,y=200)

                '''i=1
                for ro in cursor:
                    tree.insert('',i,text='',values=(i,ro[0],ro[1],ro[2],ro[3]))
                    i=i+1'''


            def account():
                global top1
                top1 = CTkToplevel()
                top1.title("Fine Management System")
            def add():
                global top3
                top3 = CTkToplevel()
                top3.title("Add Transaction+")
                top3.geometry("500x500")
                new1.attributes('-topmost', False)
                top3.attributes('-topmost',True)

                name_entry = CTkEntry(top3,width=200)
                name_entry.pack()
                inc_entry = CTkEntry(top3,width=200)
                inc_entry.pack()
                type_entry = CTkEntry(top3,width=200)
                type_entry.pack()

            
            exp_but = CTkButton(frame1,font=my_font,text = "Expenses",width=180,height=35,command = log)
            exp_but.place(x=20,y=270)

            bal_but = CTkButton(frame1,font=my_font,text = "Balance",width=180,height=35,command = balance)
            bal_but.place(x=20,y=350)

            acc_but = CTkButton(frame1,font=my_font,text = "Accounts",width=180,height=35,command = account)
            acc_but.place(x=20,y=430)

            add_but = CTkButton(frame1,font=my_font,text = "Add+",width=70,height=60,corner_radius=100,command = add)
            add_but.place(x=60,y=700)

            var1 = StringVar(value = "Monthly expense")
            var2 = StringVar(value = "Graph")
            combobox1 = CTkOptionMenu(new1,values=["Monthly expense", "Yearly expense"],variable=var1)
            combobox1.place(x=1380, y=350)

            combobox2 = CTkOptionMenu(new1,values=["Graph", "Pie-Chart"],variable=var2)
            combobox2.place(x=1380, y=400)


        
        style.use("grayscale")
        # the figure that will contain the plot
        fig = Figure(figsize = (6, 6),dpi = 100)
        
        # list of squares
        y = [i**2 for i in range(101)]
        
        # adding the subplot
        plot1 = fig.add_subplot(111)
        fig1, ax = plt.subplots(facecolor=(.18, .31, .31))
        ax.set_facecolor('#eafff5')
        
        # plotting the graph
        plot1.plot(y)
        
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig,master = new1)  
        canvas.draw()
        
        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()
        
        '''    # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas,
                                        new1)
        toolbar.update()'''
        
            # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().place(x=700,y=300)
        plt.show()
        
      
'''else:
        confirm = messagebox.showerror("Error","Wrong Password try again")
        username.delete(0,END)
        pwd.delete(0,END)'''




root.mainloop()