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
from ttkthemes import ThemedTk

root = CTk()
root.geometry("1280x800")
root.title("Fine management system")
global top2
j=0
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
        #cursor.execute("select * from transactions")
        #result = cursor.fetchall()
    
    #if username.get() in ['Sanath'] and pwd.get() in ['san']:
        confirm = messagebox.askyesno("Confirm","Are u sure")
        if confirm==True:
            root.withdraw()
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
            
            def transaction():
                mycon = sqltor.connect(host = "localhost", user = "root",passwd = "tiger",database = 'dbms')
                if mycon.is_connected() == False:
                    print("Database couldnt be connected")
                cursor = mycon.cursor()
                top2 = CTkToplevel()
                top2.title(" ")
                new1.attributes('-topmost', False)
                top2.attributes('-topmost', True)
                top2.geometry("700x500")
                top2.resizable(False,False)
                top2.minsize(width=400,height=400)
                
                s = ttk.Style(top2)
                s.theme_use("clam")
                
                cursor.execute("select * from transactions")
                #mycon.commit()

                tree = ttk.Treeview(top2)
                tree['show']='headings'
                tree['columns'] = ("Sl","Amount","Type","Date")
                tree.column('#0',width=0,minwidth=20)
                tree.column('Sl',width=150,minwidth=100)
                tree.column('Amount',width=150,minwidth=100)
                tree.column('Type',width=150,minwidth=100)
                tree.column('Date',width=150,minwidth=100)

                tree.heading('#0',text='',anchor=W)
                tree.heading('Sl',text='Sl No',anchor=W)
                tree.heading('Amount',text='Amount',anchor=W)
                tree.heading('Type',text='Type',anchor=W)
                tree.heading('Date',text='Date',anchor=W)

                scroll = CTkScrollbar(top2,orientation="vertical")
                scroll.configure(command=tree.yview)
                tree.configure(yscrollcommand=scroll.set)
                scroll.pack(ipady=150,side = RIGHT)

                tree.pack(padx = 20,pady =20)
                def remove():
                    x = tree.selection()
                    for record in x:
                         tree.delete(record)
                    print(x)
                    
                delete_but = CTkButton(top2,text = "Delete",command = remove)
                delete_but.pack(pady=20)

                i=1
                for ro in cursor:
                    tree.insert('',i,text='',values=(i,ro[0],ro[1],ro[2]))
                    i=i+1
            
            def account():
                global top1
                top1 = CTkToplevel()
                top1.title("Fine Management System")
            def add():
                top3 = CTkToplevel()
                top3.title("Add Transaction+")
                top3.geometry("500x500")
                new1.attributes('-topmost', False)
                top3.attributes('-topmost',True)
                top3.resizable(False,False)
                mycon = sqltor.connect(host = "localhost", user = "root",passwd = "tiger",database = 'dbms')
                if mycon.is_connected() == False:
                    print("Database couldnt be connected")
                cursor = mycon.cursor()

                tabview = CTkTabview(master=top3,width = 200)
                tabview.pack(padx=30, pady=20)

                spent_tab = tabview.add("     Spent     ")
                rec_tab = tabview.add(" Recieved ")

                #For spending tab
                name_label1 = CTkLabel(spent_tab,text="Name:")
                name_label1.pack()
                name_entry1 = CTkEntry(spent_tab,width=200)
                name_entry1.pack(padx=20, pady=7)
                            
                amt_label1 = CTkLabel(spent_tab,text="Amount:")
                amt_label1.pack()
                amt_entry1 = CTkEntry(spent_tab,width=200)
                amt_entry1.pack(padx=20, pady=7)

                category_label1 = CTkLabel(spent_tab,text="Category:")
                category_label1.pack()
                category_entry1 = CTkEntry(spent_tab,width=200)
                category_entry1.pack(padx=20, pady=7)

                date_label1 = CTkLabel(spent_tab,text="Date:")
                date_label1.pack()
                date_entry1 = CTkEntry(spent_tab,width=200)
                date_entry1.pack(padx=20, pady=7)

                #For recieved money tab
                amt_label2 = CTkLabel(rec_tab,text="Amount:")
                amt_label2.pack()
                amt_entry2 = CTkEntry(rec_tab,width=200)
                amt_entry2.pack(padx=20, pady=10)

                '''category_label2 = CTkLabel(rec_tab,text="Category:")
                category_label2.pack()
                category_entry2 = CTkEntry(rec_tab,width=200)
                category_entry2.pack(padx=20, pady=10)'''

                date_label2 = CTkLabel(rec_tab,text="Date:")
                date_label2.pack()
                date_entry2 = CTkEntry(rec_tab,width=200)
                date_entry2.pack(padx=20, pady=10)
                def add_button1():
                    global j
                    j=j+1
                    if spent_tab:
                        amt1 = amt_entry1.get()
                        name1 = name_entry1.get()
                        cate1 = category_entry1.get()
                        date1 = date_entry1.get()

                        if not amt1 and not name1  and not cate1  and not date1 :
                            errors = messagebox.showerror("Error","Please fill all the tables!",parent = spent_tab)
                            return

                        insert1 = "insert into expenses(Name,Amount,Category,UserID,Date) values('{}',{},'{}','{}','{}')".format(name1,amt1,cate1,'Sanath',date1)
                        cursor.execute(insert1)
                        mycon.commit()

                        tup1 = (j,amt1,date1)
                        q1 = """Call transactiondeb(%s,%s,%s);"""
                        cursor.execute(q1,tup1)
                        mycon.commit()
                        
                        debit = """Call debit(%s,'Sanath')"""
                        tuple1 = (amt1,)
                        cursor.execute(debit,tuple1)
                        mycon.commit()
                        successful1 = messagebox.showinfo("Congrats!", "Transaction Added Successfully",parent = spent_tab)


                def add_button2():
                    global j
                    j=j+1
                    if rec_tab:
                        amt2 = amt_entry2.get()
                        date2 = date_entry2.get()
                        if not amt2 and not date2 :
                            messagebox.showerror("Error","Please fill all the tables!",parent = rec_tab)
                            return
                        
                        insert2 = "insert into income(Amount,UserID,Date) values({},'{}','{}')".format(amt2,'Sanath',date2)
                        cursor.execute(insert2)
                        mycon.commit()

                        
                        tup2 = (j,amt2,date2)
                        q2 = """Call transactioncred(%s,%s,%s);"""
                        cursor.execute(q2,tup2)
                        mycon.commit()
                        
                        credit = """Call credit(%s,'Sanath')"""
                        tuple2 = (amt2,)
                        cursor.execute(credit,tuple2)
                        mycon.commit()
                        successful2 = messagebox.showinfo("Congrats!", "Transaction Added Successfully",parent = rec_tab)

                add_button1 = CTkButton(spent_tab,text = "Add",height=30,width=200,command=add_button1)
                add_button1.pack(pady=40)

                add_button2 = CTkButton(rec_tab,text = "Add",width=200,command=add_button2)
                add_button2.pack(pady=40)

            
            exp_but = CTkButton(frame1,font=my_font,text = "Spend Analytics",width=180,height=35,command = log)
            exp_but.place(x=20,y=270)

            expenses_but = CTkButton(frame1,font=my_font,text = "Expenses",width=180,height=35,command = transaction)
            expenses_but.place(x=20,y=350)

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


        
'''style.use("grayscale")
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
        
            # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas,
                                        new1)
        toolbar.update()
        
            # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().place(x=700,y=300)
        plt.show()
        
      
    else:
        confirm = messagebox.showerror("Error","Wrong Password try again")
        username.delete(0,END)
        pwd.delete(0,END)
    '''



mycon.close()
root.mainloop()