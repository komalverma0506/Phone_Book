from tkinter import *
import pymysql as sql
root = Tk()

def save_contact():
    global ent1,ent2
    gui = Tk()
    name = ent1.get()
    number = ent2.get()
    root.destroy()
        
    try:
        db = sql.connect(host='localhost',port=3306,user='root',password='',database='contact')
        cur=db.cursor()
        cmd = f"insert into data values('{name}','{number}')"
        cur.execute(cmd)
        db.commit()
        
    except Exception as e:
        lb = Label(gui,text=e,fg='red',font=('Times',20,'bold'))
        lb.pack(pady=30)
    else:
        lb = Label(gui,text='Contact Saved Successfully',fg='green',font=('Times',20,'bold'))
        lb.pack(pady=30)
    finally:
        btn = Button(gui,text='Exit',command=gui.destroy,width=10)
        btn.pack()
    
        btn1 = Button(gui,text='Show',command=show1,width=10)
        btn1.pack()
        
        btn2  = Button(gui,text='Save New Contact',command=save1,width=20)
        btn2.pack()

    gui.mainloop()
    
def save_contact1():
    global ent1,ent2
    gui3 = Tk()
    name = ent1.get()
    number = ent2.get()
        
    try:
        db = sql.connect(host='localhost',port=3306,user='root',password='',database='contact')
        cur=db.cursor()
        cmd = f"insert into data values('{name}','{number}')"
        cur.execute(cmd)
        db.commit()
        
    except Exception as e:
        lb = Label(gui3,text=e,fg='red',font=('Times',20,'bold'))
        lb.pack(pady=30)
    else:
        lb = Label(gui3,text='Contact Saved Successfully',fg='green',font=('Times',20,'bold'))
        lb.pack(pady=30)
    finally:
        btn = Button(gui3,text='Exit',command=gui3.destroy,width=10)
        btn.pack()

    gui3.mainloop()
    
def show_contact():
    global ent1,ent2
    gui = Tk()
    name = ent1.get()
    root.destroy()
    
    try:
        db = sql.connect(host='localhost',port=3306,user='root',password='',database='contact')
        cur=db.cursor()
        cmd = f"select * from data where name like '{name}%'"
        cur.execute(cmd)
        data = cur.fetchall()
        if not(data):
            raise FileNotFoundError('No Contact Found')
    except Exception as e:
        lb = Label(gui,text=e,fg='red',font=('Times',20,'bold'))
        lb.pack(pady=30,padx=30)
    else:
        for i in range(len(data)):
                lb = Label(gui,text=list(data[i]),fg='green',font=('Times',20,'bold'))
                lb.pack()
    finally:
        btn = Button(gui,text='Exit',command=gui.destroy,width=10)
        btn.pack()

    
    gui.mainloop()
    
def show_contact1():
    global ent1,ent2
    gui1 = Tk()
    name = ent1.get()
    
    
    try:
        db = sql.connect(host='localhost',port=3306,user='root',password='',database='contact')
        cur=db.cursor()
        cmd = f"select * from data where name like '{name}%'"
        cur.execute(cmd)
        data = cur.fetchall()
        if not(data):
            raise FileNotFoundError('No Contact Found')
    except Exception as e:
        lb = Label(gui1,text=e,fg='red',font=('Times',20,'bold'))
        lb.pack(pady=30,padx=30)
    else:
        for i in range(len(data)):
                lb = Label(gui1,text=list(data[i]),fg='green',font=('Times',20,'bold'))
                lb.pack()
    finally:
        btn = Button(gui1,text='Exit',command=gui1.destroy,width=10)
        btn.pack()
    gui1.mainloop()

def save():
    global ent1,ent2
    lb_1.destroy()
    lb_2.destroy()
    bt1.destroy()
    bt2.destroy()
    
    lb1 = Label(root,text='Enter Name',font=('Times',10,'bold'))
    lb1.grid(row=0,column=0)
    lb2 = Label(root,text='Enter Number',font=('Times',10,'bold'))
    lb2.grid(row=1,column=0)
    ent1 = Entry(root,font=('Times',10,'bold'))
    ent1.grid(row=0,column=1)
    ent2 = Entry(root,font=('Times',10,'bold'))
    ent2.grid(row=1,column=1)
    
    bt = Button(root,text='Save',font=('Times',20,'italic'),command=save_contact,width=10)
    bt.grid(row=2,columnspan=2,pady=40)
    
def save1():
    global ent1,ent2
    gui2 = Tk()
    
    lb1 = Label(gui2,text='Enter Name',font=('Times',10,'bold'))
    lb1.grid(row=0,column=0)
    lb2 = Label(gui2,text='Enter Number',font=('Times',10,'bold'))
    lb2.grid(row=1,column=0)
    ent1 = Entry(gui2,font=('Times',10,'bold'))
    ent1.grid(row=0,column=1)
    ent2 = Entry(gui2,font=('Times',10,'bold'))
    ent2.grid(row=1,column=1)
    
    bt = Button(gui2,text='Save',font=('Times',20,'italic'),command=save_contact1,width=10)
    bt.grid(row=2,columnspan=2,pady=40)
    
    btn = Button(gui2,text='Exit',font=('Times',20,'italic'),command=gui2.destroy,width=10)
    btn.grid(row=3,columnspan=2)
    
    gui2.mainloop()

def show():
    global ent1,ent2
    lb_1.destroy()
    lb_2.destroy()
    bt1.destroy()
    bt2.destroy()
    
    lb1 = Label(root,text='Enter Name',font=('Times',10,'bold'))
    lb1.grid(row=0,column=0)
    
    ent1 = Entry(root,font=('Times',10,'bold'))
    ent1.grid(row=0,column=1)
    
    bt = Button(root,text='Show',font=('Times',20,'italic'),command=show_contact,width=10)
    bt.grid(row=3,columnspan=2,pady=40)
    
def show1():
    global ent1,ent2   
    gui = Tk()
    lb1 = Label(gui,text='Enter Name',font=('Times',10,'bold'))
    lb1.grid(row=0,column=0)
    
    ent1 = Entry(gui,font=('Times',10,'bold'))
    ent1.grid(row=0,column=1)
    
    bt = Button(gui,text='Show',font=('Times',20,'italic'),command=show_contact1,width=10)
    bt.grid(row=3,columnspan=2,pady=40)
    
    btn = Button(gui,text='Exit',font=('Times',20,'italic'),command=gui.destroy,width=10)
    btn.grid(row=4,columnspan=2)
    
    gui.mainloop()

lb_1 = Label(root,text='PhoneBook Dictionary',font=('Times',20,'bold'))    
lb_1.grid(row=0,columnspan=3)
lb_2 = Label(root,text='Please Choose One Option',font=('Times',10,'italic'))    
lb_2.grid(row=1,columnspan=3)   

bt1 = Button(root,text='Add Contact',font=('Times',20,'italic'),command=save,width=20)
bt1.grid(row=2,columnspan=3,pady=40)
bt2 = Button(root,text='Search Contact',font=('Times',20,'italic'),command=show,width=20)
bt2.grid(row=3,columnspan=3)

root.mainloop()
