from tkinter import *
from customtkinter import*
from tkinter import ttk,font
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector as sqltor
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
username.place(x=645,y=330)

pwdlabel = CTkLabel(root,text="Password")
pwdlabel.place(x=560,y=410)
pwd = CTkEntry(root,width=250)
pwd.configure(show="*")
pwd.place(x=645,y=410)
login = CTkButton(root,text='Login',command=lambda:log())
login.place(x=680,y=500)

def log():
    mycon = sqltor.connect(host = "localhost", user = "root",passwd = "tiger",database = 'dbms')
    if mycon.is_connected() == False:
        print("Database couldnt be connected")
    cursor = mycon.cursor()
    cursor.execute("select * from users")
    result = cursor.fetchall()
    password = ['','']
    user = username.get()
    pasw = pwd.get()
    i=0
    for passw in result:
        password[i] = passw
        i=i+1

    if username.get() == password[0][0] and pwd.get() == password[0][1] or username.get() == password[1][0] and pwd.get() == password[1][1]:
        confirm = messagebox.askyesno("Confirm","Are u sure")
        if confirm==True:
            root.withdraw()
            new1 = CTkToplevel()
            new1.attributes('-topmost', True)
            new1.title("Spend Analytics")
            new1.geometry("1280x800")
            
            
            def create_frame():
                global frame1,frame2
                frame1 = CTkFrame(new1,height=830,width=240)
                frame1.place(x=0,y=0)
                frame2 = CTkFrame(new1,height=100,width=1265)
                frame2.place(x=260,y=0)

            frame3 = CTkFrame(new1,height=710,width=1100)
            frame3.place(x=260,y=120)
            my_font = CTkFont(family="<Futura>",size = 12)

            cate_frame = CTkFrame(frame3,width = 400,height=280)
            cate_frame.place(x=600,y=99)

            cate_label = CTkLabel(cate_frame,text="Enter Categories:")
            #cate_label.place(x=150,y=15)
            cate_label.pack(padx=20,pady=10)

            cate_entry = CTkEntry(cate_frame,width=200)
            cate_entry.pack(padx=80,pady=15)

            

            def cate():
                cate = CTkToplevel()
                cate.attributes('-topmost',True)
                new1.attributes('-topmost',False)

                mycon = sqltor.connect(host = "localhost", user = "root",passwd = "tiger",database = 'dbms')
                if mycon.is_connected() == False:
                    print("Database couldnt be connected")
                cursor = mycon.cursor()

                c = cate_entry.get()
                cate_query = """Call categoryexpense(%s,%s);"""
                cate_tuple = (c,user)
                cursor.execute(cate_query,cate_tuple)
                result = cursor.fetchall()

                cate_tree = ttk.Treeview(cate)
                s = ttk.Style(cate)
                s.theme_use("clam")
                s.configure("cate_tree",background="white",foreground = "black",rowheight=25,fieldbackground="white")
                cate_tree['show']='headings'
                cate_tree['columns'] = ("Item","Amount","Date")
                cate_tree.column('#0',width=0,minwidth=20)
                cate_tree.column('Item',width=150,minwidth=150,anchor=W)
                cate_tree.column('Amount',width=150,minwidth=150,anchor=CENTER)
                cate_tree.column('Date',width=150,minwidth=150,anchor=CENTER)

                cate_tree.heading('#0',text='',anchor=CENTER)
                cate_tree.heading('Item',text='Item',anchor=CENTER)
                cate_tree.heading('Amount',text='Amount',anchor=CENTER)
                cate_tree.heading('Date',text='Date',anchor=CENTER)

                l=1
                for rows in result:
                    cate_tree.insert('',l,text='',values=(rows[0],rows[1],rows[2]))
                    l=l+1
                cate_tree.pack(padx=20,pady=20)
                mycon.close()

            cate_button = CTkButton(cate_frame,width=100,text="Category Expense",command=cate)
            cate_button.pack(pady=10)

            def cate_wise():
                cate_wise = CTkToplevel()
                cate_wise.attributes('-topmost',True)
                cate_wise.title(" ")
                new1.attributes('-topmost',False)

                mycon = sqltor.connect(host = "localhost", user = "root",passwd = "tiger",database = 'dbms')
                if mycon.is_connected() == False:
                    print("Database couldnt be connected")
                cursor = mycon.cursor()

                cate_wise_query = """Call Categorywise(%s);"""
                cate_wise_tuple = (user,)
                cursor.execute(cate_wise_query,cate_wise_tuple)
                res = cursor.fetchall()
                
                cate_wise_tree = ttk.Treeview(cate_wise)
                s = ttk.Style(cate_wise)
                s.theme_use("clam")
                cate_wise_tree['show']='headings'
                cate_wise_tree['columns'] = ("Category","Amount")
                cate_wise_tree.column('#0',width=0,minwidth=20)
                cate_wise_tree.column('Category',width=200,minwidth=200,anchor=W)
                cate_wise_tree.column('Amount',width=150,minwidth=150,anchor=CENTER)

                cate_wise_tree.heading('#0',text='',anchor=CENTER)
                cate_wise_tree.heading('Category',text='Category',anchor=CENTER)
                cate_wise_tree.heading('Amount',text='Amount',anchor=CENTER)

                l=1
                for rows in res:
                    cate_wise_tree.insert('',l,text='',values=(rows[0],rows[1]))
                    l=l+1
                cate_wise_tree.pack(padx=20,pady=20)


            cate_wise_button = CTkButton(cate_frame,width = 120,text="Category Wise \n Total Expense",command=cate_wise)
            cate_wise_button.pack(pady=25)


            mon_year_tab = CTkTabview(frame3,width=400,height = 270)
            mon_year_tab.place(x=90,y=80)

            Month = mon_year_tab.add("   Month   ")
            Year = mon_year_tab.add("   Year   ")

            exp_month_label = CTkLabel(Month,text="Enter Month:")
            exp_month_label.pack(pady=5)

            exp_month_entry = CTkEntry(Month,width = 200)
            exp_month_entry.pack(pady=10)

            acc_label = CTkLabel(frame3,text = "Account Balance:")
            acc_label.place(x=90,y=500)

            def month_all_exp():
                expense = CTkToplevel()
                expense.title(" ")
                expense.attributes('-topmost',True)
                new1.attributes('-topmost',False)
                mycon = sqltor.connect(host = "localhost", user = "root",passwd = "tiger",database = 'dbms')
                if mycon.is_connected() == False:
                    print("Database couldnt be connected")
                cursor = mycon.cursor()
                exp = exp_month_entry.get()
                all_exp_query = """Call ExpenseMonth(%s,%s);"""
                exp_tup = (exp,user)
                cursor.execute(all_exp_query,exp_tup)
                result = cursor.fetchall()
                
                exp_tree = ttk.Treeview(expense)
                s = ttk.Style(expense)
                s.theme_use("clam")
                exp_tree['show']='headings'
                exp_tree['columns'] = ("Item","Amount","Category","Date")
                exp_tree.column('#0',width=0,minwidth=20)
                exp_tree.column('Item',width=150,minwidth=150,anchor=W)
                exp_tree.column('Amount',width=150,minwidth=150,anchor=CENTER)
                exp_tree.column('Category',width=150,minwidth=150,anchor=CENTER)
                exp_tree.column('Date',width=200,minwidth=150,anchor=CENTER)

                exp_tree.heading('#0',text='',anchor=CENTER)
                exp_tree.heading('Item',text='Item',anchor=CENTER)
                exp_tree.heading('Amount',text='Amount',anchor=CENTER)
                exp_tree.heading('Category',text='Category',anchor=CENTER)
                exp_tree.heading('Date',text='Date',anchor=CENTER)

                l=1
                for rows in result:
                    exp_tree.insert('',l,text='',values=(rows[0],rows[1],rows[2],rows[3]))
                    l=l+1

                exp_tree.pack(padx = 20,pady =20)


            exp_month_button1 = CTkButton(Month,text="All Expenses",width=80,command=month_all_exp)
            exp_month_button1.pack(pady=10)

            def month_tot_exp():
                tot = CTkToplevel()
                tot.title(" ")
                tot.attributes('-topmost',True)
                new1.attributes('-topmost',False)
                mycon = sqltor.connect(host = "localhost", user = "root",passwd = "tiger",database = 'dbms')
                if mycon.is_connected() == False:
                    print("Database couldnt be connected")
                cursor = mycon.cursor()

                tot_frame = CTkFrame(tot,width=50,height=50)
                tot_frame.pack(padx=20,pady=20)

                exp = exp_month_entry.get()
                tot_exp_query = """Call TotalMonth(%s,%s);"""
                tot_exp_tup = (exp,user)
                cursor.execute(tot_exp_query,tot_exp_tup)
                a = ['']
                for i in cursor:
                    a[0] = i

                tot_exp_label = CTkLabel(tot_frame,text="The total Expense is"+str(a[0][0]))
                tot_exp_label.pack(padx=30,pady=30)


            exp_month_button2 = CTkButton(Month,text="Total Expense",width=80,command=month_tot_exp)
            exp_month_button2.pack(pady=10)

            exp_year_label = CTkLabel(Year,text="Enter Year:")
            exp_year_label.pack(pady=5)

            exp_year_entry = CTkEntry(Year,width = 200)
            exp_year_entry.pack(pady=10)

            def year_all_exp():
                y_expense = CTkToplevel()
                y_expense.title(" ")
                y_expense.attributes('-topmost',True)
                new1.attributes('-topmost',False)
                mycon = sqltor.connect(host = "localhost", user = "root",passwd = "tiger",database = 'dbms')
                if mycon.is_connected() == False:
                    print("Database couldnt be connected")
                cursor = mycon.cursor()
                exp = exp_year_entry.get()
                all_exp_query = """Call ExpenseYear(%s,%s);"""
                y_exp_tup = (exp,user)
                cursor.execute(all_exp_query,y_exp_tup)
                result = cursor.fetchall()
                
                y_exp_tree = ttk.Treeview(y_expense)
                s = ttk.Style(y_expense)
                s.theme_use("clam")
                y_exp_tree['show']='headings'
                y_exp_tree['columns'] = ("Item","Amount","Category","Date")
                y_exp_tree.column('#0',width=0,minwidth=20)
                y_exp_tree.column('Item',width=150,minwidth=150,anchor=W)
                y_exp_tree.column('Amount',width=150,minwidth=150,anchor=CENTER)
                y_exp_tree.column('Category',width=150,minwidth=150,anchor=CENTER)
                y_exp_tree.column('Date',width=150,minwidth=150,anchor=CENTER)

                y_exp_tree.heading('#0',text='',anchor=CENTER)
                y_exp_tree.heading('Item',text='Item',anchor=CENTER)
                y_exp_tree.heading('Amount',text='Amount',anchor=CENTER)
                y_exp_tree.heading('Category',text='Category',anchor=CENTER)
                y_exp_tree.heading('Date',text='Date',anchor=CENTER)

                l=1
                for rows in result:
                    y_exp_tree.insert('',l,text='',values=(rows[0],rows[1],rows[2],rows[3]))
                    l=l+1

                y_exp_tree.pack(padx = 20,pady =20)

            exp_year_button1 = CTkButton(Year,text="All Expenses",width=80,command = year_all_exp)
            exp_year_button1.pack(pady=10)

            def year_tot_exp():
                y_tot = CTkToplevel()
                y_tot.title(" ")
                y_tot.attributes('-topmost',True)
                new1.attributes('-topmost',False)
                mycon = sqltor.connect(host = "localhost", user = "root",passwd = "tiger",database = 'dbms')
                if mycon.is_connected() == False:
                    print("Database couldnt be connected")
                cursor = mycon.cursor()

                y_tot_frame = CTkFrame(y_tot,width=50,height=50)
                y_tot_frame.pack(padx=20,pady=20)

                y_exp = exp_year_entry.get()
                y_tot_exp_query = """Call TotalYear(%s,%s);"""
                y_tot_exp_tup = (y_exp,user)
                cursor.execute(y_tot_exp_query,y_tot_exp_tup)
                a = ['']
                for i in cursor:
                    a[0] = i

                tot_exp_label = CTkLabel(y_tot_frame,text="The total Expense is "+str(a[0][0]))
                tot_exp_label.pack(padx=30,pady=30)


            exp_year_button2 = CTkButton(Year,text="Total Expense",width=80,command=year_tot_exp)
            exp_year_button2.pack(pady=10)

            create_frame()
            Welcome = CTkButton(frame1,font=my_font,text = "Welcome Back\n"+username.get(),width=180,height=60)
            Welcome.place(x=20,y=25)

            def Calc():
                win = CTk()
                win.attributes('-topmost',True)
                new1.attributes('-topmost',False)
                win.resizable(False,False)

                win.title("Calculator")
                e=CTkEntry(win,width=200)
                e.grid(row=0,column=0,columnspan=3,padx=2,pady=12) #3 Column Spaces under column

                def button_click(number):
                    current=e.get()
                    e.delete(0,END)
                    e.insert(0,str(current)+str(number))

                def button_clear():
                    e.delete(0,END)

                def button_add():
                    first_no=e.get()
                    global f_num
                    global math
                    math="addition"
                    f_num=first_no
                    e.delete(0,END)

                def button_subtract():
                    first_no=e.get()
                    global f_num
                    global math
                    math="subtraction"
                    f_num=first_no
                    e.delete(0,END)
                    
                def button_multiply():
                    first_no=e.get()
                    global f_num
                    global math
                    math="multiplication"
                    f_num=first_no
                    e.delete(0,END)

                def button_divide():
                    first_no=e.get()
                    global f_num
                    global math
                    math="division"
                    f_num=first_no
                    e.delete(0,END)

                def button_equal():
                    global f_num
                    global math
                    a="/"
                    global second_no
                    second_no=e.get()
                    if second_no==0:
                        pass
                    elif f_num==0:
                        pass

                    if math=="addition":
                        e.delete(0,END)
                        e.insert(0,int(f_num)+int(second_no))
                    elif math=="subtraction":
                        e.delete(0,END)
                        e.insert(0,int(f_num)-int(second_no))
                    elif math=="multiplication":
                        e.delete(0,END)
                        e.insert(0,int(f_num)*int(second_no))
                    elif math=="division":
                        e.delete(0,END)
                        c=second_no
                        try:
                            e.insert(0,int(f_num)/int(second_no))
                        except:
                            second_no="Error!!! Click Clear"
                            e.insert(0,second_no)
                        try:
                            button_equal()
                        except:
                            pass
                        
                    else:
                        e.delete(0,END)
                    
                #Buttons     
                button_1=Button(win,text="    1   ",padx=30,pady=20,command=lambda: button_click(1)).grid(row=3,column=0)
                button_2=Button(win,text="2",padx=40,pady=20,command=lambda: button_click(2)).grid(row=3,column=1)
                button_3=Button(win,text="3",padx=40,pady=20,command=lambda: button_click(3)).grid(row=3,column=2)

                button_4=Button(win,text="    4   ",padx=30,pady=20,command=lambda:button_click(4)).grid(row=2,column=0)
                button_5=Button(win,text="5",padx=40,pady=20,command=lambda:button_click(5)).grid(row=2,column=1)
                button_6=Button(win,text="6",padx=40,pady=20,command=lambda:button_click(6)).grid(row=2,column=2)

                button_7=Button(win,text="    7   ",padx=30,pady=20,command=lambda:button_click(7)).grid(row=1,column=0)
                button_8=Button(win,text="8",padx=40,pady=20,command=lambda:button_click(8)).grid(row=1,column=1)
                button_9=Button(win,text="9",padx=40,pady=20,command=lambda:button_click(9)).grid(row=1,column=2)

                button_0 =Button(win,text="0",padx=40,pady=20,command=lambda:button_click(0)).grid(row=4,column=1)

                button_add=Button(win,text="  +",padx=37.5,pady=20,command=button_add).grid(row=1,column=3)
                button_equal=Button(win,text="=",padx=39,pady=20,command=button_equal).grid(row=4,column=2,)
                button_clear=Button(win,text="Clear ",padx=30,pady=20,command=button_clear).grid(row=4,column=0)

                button_subtract=Button(win,text="  -",padx=40,pady=20,command=button_subtract).grid(row=2,column=3)
                button_multiply=Button(win,text=" X ",padx=38,pady=20,command=button_multiply).grid(row=3,column=3)
                button_divide=Button(win,text="  /",padx=40,pady=20,command=button_divide).grid(row=4,column=3)
                button_exit=Button(win,text="Exit",padx=20,pady=15,command=win.destroy).grid(row=0,column=3)
                win.mainloop()
            calc = CTkButton(frame1,text="Calculator",height=70,command=Calc)
            calc.place(x=40,y=300)

            Exp_button = CTkButton(frame2,text="Spend Analytics",width = 200,height = 35)
            Exp_button.place(x=430,y=25)
            
            #Profile Button for updating Password
            def prof():
                prof = CTkToplevel()
                prof.attributes('-topmost',True)
                prof.title("Update Password")
                new1.attributes('-topmost', False)

                update_label1 = CTkLabel(prof,text="---------------------------------------------------------")
                update_label1.pack()

                update_label = CTkLabel(prof,text="Update Password")
                update_label.pack()

                update_label2 = CTkLabel(prof,text="---------------------------------------------------------")
                update_label2.pack()

                old_pwd_label = CTkLabel(prof,text="Enter Old Password:")
                old_pwd_label.pack()
                old_pwd_entry = CTkEntry(prof,width=200)
                old_pwd_entry.pack(padx=20,pady=10)

                new_pwd_label = CTkLabel(prof,text="Enter New Password:")
                new_pwd_label.pack()
                new_pwd_entry = CTkEntry(prof,width=200)
                new_pwd_entry.pack(padx=20,pady=10)

                def submit():
                    mycon = sqltor.connect(host = "localhost", user = "root",passwd = "tiger",database = 'dbms')
                    if mycon.is_connected() == False:
                        print("Database couldnt be connected")
                    cursor = mycon.cursor()

                    old_pwd = old_pwd_entry.get()
                    new_pwd = new_pwd_entry.get()
                    new_tuple = (old_pwd,new_pwd)

                    change_pwd_query = """Call ChangePassword(%s,%s);"""
                    cursor.execute(change_pwd_query,new_tuple)

                    mycon.commit()
                    mycon.close()
                    messagebox.showinfo("Congrats!", "Password Changed Successfully",parent = prof)

                submit_pwd = CTkButton(prof,text="Change Password",command=submit)
                submit_pwd.pack(pady=10)            

            profile_button = CTkButton(frame2,text="Profile",width=100,height=50,command=prof)
            profile_button.place(x=1150,y=20)
            
            #To display all the transactions that have occured (Expenses)
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

                tree = ttk.Treeview(top2)

                tree['show']='headings'
                tree['columns'] = ("Sl","Amount","Date","Type")
                tree.column('#0',width=0,minwidth=20)
                tree.column('Sl',width=50,minwidth=50,anchor=W)
                tree.column('Amount',width=150,minwidth=150,anchor=CENTER)
                tree.column('Date',width=150,minwidth=150,anchor=CENTER)
                tree.column('Type',width=150,minwidth=150,anchor=CENTER)

                tree.heading('#0',text='',anchor=CENTER)
                tree.heading('Sl',text='Sl No',anchor=CENTER)
                tree.heading('Amount',text='Amount',anchor=CENTER)
                tree.heading('Date',text='Date',anchor=CENTER)
                tree.heading('Type',text='Type',anchor=CENTER)

                scroll = CTkScrollbar(top2,orientation="vertical")
                scroll.configure(command=tree.yview)
                tree.configure(yscrollcommand=scroll.set)
                scroll.pack(ipady=150,side = RIGHT)

                tree.pack(padx = 20,pady =20)

                #Adds rows to transaction table(expenses tables)
                i=1
                for ro in cursor:
                    tree.insert('',i,text='',values=(i,ro[1],ro[3],ro[2]))
                    i=i+1

                #Function to add/delete category names
                def callback(value):
                        mycon = sqltor.connect(host = "localhost", user = "root",passwd = "tiger",database = 'dbms')
                        if mycon.is_connected() == False:
                            print("Database couldnt be connected")
                        cursor = mycon.cursor()
                        if value =="  Add  ":
                            add_val = entry.get()
                            adding = """Call AddCategory(%s);"""
                            t1=(add_val,)
                            cursor.execute(adding,t1)
                            
                            mycon.commit()
                            messagebox.showinfo("Congrats!", "Category Added Successfully",parent = top2)

                        elif value ==" Delete ":
                            print("bye")
                            del_val = entry.get()
                            deleting = """Call RemoveCategory(%s);"""
                            t2=(del_val,)
                            cursor.execute(deleting,t2)
                            
                            mycon.commit()
                            messagebox.showinfo("Congrats!", "Category Removed Successfully",parent = top2)
                        mycon.close()
               

                add_del_label = CTkLabel(top2,text="Enter Category Name")
                add_del_label.pack()

                entry = CTkEntry(top2,width=200)
                entry.pack(padx=20,pady=10)

                add_del_cate = CTkSegmentedButton(top2,values=["  Add  "," Delete "],command=callback)
                add_del_cate.pack(padx=20,pady=10)

                #Function to show all the categories that have been made
                def show():
                    temp = CTkToplevel()
                    new1.attributes('-topmost', False)
                    top2.attributes('-topmost', False)
                    temp.attributes('-topmost',True)
                    temp.title("Categories")
                    mycon = sqltor.connect(host = "localhost", user = "root",passwd = "tiger",database = 'dbms')
                    if mycon.is_connected() == False:
                        print("Database couldnt be connected")
                    cursor = mycon.cursor()

                    temp_tree = ttk.Treeview(temp)
                    s_temp = ttk.Style(temp)
                    s_temp.theme_use("clam")
                    temp_tree['show']='headings'
                    temp_tree['columns'] = ("Category")
                    temp_tree.column('#0',width=0,minwidth=20)
                    temp_tree.column('Category',width=150,minwidth=100)
                    temp_tree.heading('#0',text='',anchor=W)
                    temp_tree.heading('Category',text='Category Names',anchor=W)
                    all_cate_query = """Call AllCategories(%s);"""
                    all_cate_tuple = (user,)
                    cursor.execute(all_cate_query,all_cate_tuple)
                    result = cursor.fetchall()

                    temp_tree.pack(padx=30,pady=30)
                    
                    k=1
                    for rows in result:
                        temp_tree.insert('',k,text='',values=rows[0])
                        k=k+1
                mycon.close()
                show_cate = CTkButton(top2,text="List of Categories",command = show)
                show_cate.pack(pady=20)

                top2.mainloop()
            
            mycon.close()

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

                        insert1 = "insert into expenses(Item,Amount,Category,UserID,Date) values('{}',{},'{}','{}','{}')".format(name1,amt1,cate1,user,date1)
                        cursor.execute(insert1)
                        mycon.commit()

                        tup1 = (j,amt1,date1)
                        q1 = """Call transactiondeb(%s,%s,%s);"""
                        cursor.execute(q1,tup1)
                        mycon.commit()
                        
                        debit = """Call debit(%s,%s)"""
                        tuple1 = (amt1,user)
                        cursor.execute(debit,tuple1)
                        mycon.commit()
                        successful1 = messagebox.showinfo("Congrats!", "Transaction Added Successfully",parent = spent_tab)
                        prog_query = """select Balance from Users where UserId = %s"""
                        prog_tuple = (user,)
                        cursor.execute(prog_query,prog_tuple)
                        val = cursor.fetchall()
                        l = ['']
                        for va in val:
                            l[0] = va

                        balance_label = CTkLabel(frame3,text="    "+str(l[0][0]))
                        balance_label.place(x=250,y=500)
                
                


                def add_button2():
                    global j
                    j=j+1
                    if rec_tab:
                        amt2 = amt_entry2.get()
                        date2 = date_entry2.get()
                        if not amt2 and not date2 :
                            messagebox.showerror("Error","Please fill all the tables!",parent = rec_tab)
                            return
                        
                        insert2 = "insert into income(Amount,UserID,Date) values({},'{}','{}')".format(amt2,user,date2)
                        cursor.execute(insert2)
                        mycon.commit()

                        
                        tup2 = (j,amt2,date2)
                        q2 = """Call transactioncred(%s,%s,%s);"""
                        cursor.execute(q2,tup2)
                        mycon.commit()
                        
                        credit = """Call credit(%s,%s)"""
                        tuple2 = (amt2,user)
                        cursor.execute(credit,tuple2)
                        mycon.commit()
                        successful2 = messagebox.showinfo("Congrats!", "Transaction Added Successfully",parent = rec_tab)

                        prog_query = """select Balance from Users where UserId = %s"""
                        prog_tuple = (user,)
                        cursor.execute(prog_query,prog_tuple)
                        val = cursor.fetchall()
                        l = ['']
                        for va in val:
                            l[0] = va

                        balance_label = CTkLabel(frame3,text="    "+str(l[0][0]))
                        balance_label.place(x=250,y=500)

                add_button1 = CTkButton(spent_tab,text = "Add",height=30,width=200,command=add_button1)
                add_button1.pack(pady=40)

                add_button2 = CTkButton(rec_tab,text = "Add",width=200,command=add_button2)
                add_button2.pack(pady=40)

                

            expenses_but = CTkButton(new1,font=my_font,text = "Expenses",width=150,height=35,command = transaction)
            expenses_but.place(x=1375,y=280)

            def max_min():
                mycon = sqltor.connect(host = "localhost", user = "root",passwd = "tiger",database = 'dbms')
                if mycon.is_connected() == False:
                    print("Database couldnt be connected")
                cursor = mycon.cursor()
                max_min = CTkToplevel()
                max_min.geometry("300x300")
                max_min.attributes('-topmost',True)
                new1.attributes('-topmost',False)

                new_tuple = (user,)
                max_query = """Call MaxCategory(%s);"""

                min_query = """Call MinCategory(%s);"""
                

                cursor.execute(max_query,new_tuple)
                res = cursor.fetchall()
                a = [' ',' ']
                j=0
                for i in res:
                    a[j] = i
                    j=j+1

                max_frame = CTkFrame(max_min,width = 205,height = 200)
                max_frame.pack(padx=20,pady=20)

                max_label = CTkLabel(max_frame,text = "The Maximum Expenditure Category is\n\n"+a[0][0]+":\n"+str(a[0][1]))
                max_label.pack(padx=20,pady=20)
                
                mycon.close()

                mycon = sqltor.connect(host = "localhost", user = "root",passwd = "tiger",database = 'dbms')
                if mycon.is_connected() == False:
                    print("Database couldnt be connected")
                cursor = mycon.cursor()
                cursor.execute(min_query,new_tuple)
                res1 = cursor.fetchall()
                a1 = [' ',' ']
                j=0
                for i in res1:
                    a1[j] = i
                    j=j+1

                min_frame = CTkFrame(max_min,width = 205,height = 200)
                min_frame.pack(padx=20,pady=20)

                min_label = CTkLabel(min_frame,text = "The Minimum Expenditure Category is\n\n"+a1[0][0]+":\n"+str(a1[0][1]))
                min_label.pack(padx=20,pady=30)
                

            expenses_overview = CTkButton(new1,text="Expenditure\n Overview" ,width=150,height=35,command = max_min)
            expenses_overview.place(x=1375,y=360)

            exit_button = CTkButton(new1, text="Exit", command=root.destroy,height=40)
            exit_button.place(x=1375,y=740)

            add_but = CTkButton(frame1,font=my_font,text = "Add+",width=70,height=60,corner_radius=100,command = add)
            add_but.place(x=60,y=720)

            progressbar = CTkProgressBar(master=frame3,width=550,height=20)
            progressbar.place(y=580, x=200)

            
            #progressbar.start()
            mycon = sqltor.connect(host = "localhost", user = "root",passwd = "tiger",database = 'dbms')
            if mycon.is_connected() == False:
                print("Database couldnt be connected")
            cursor = mycon.cursor()

           

            new1.mainloop()


        
    else:
        confirm = messagebox.showerror("Error","Wrong Password try again")
        username.delete(0,END)
        pwd.delete(0,END)

mycon.close()
root.mainloop()