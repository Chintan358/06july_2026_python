from tkinter import *
import mysql.connector as sql

con = sql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="6july_python"
)
cursor  =con.cursor()
# print(con.is_connected())

root = Tk()
root.geometry("500x500")
root.title("Myapp")



def get_data():
   name = t1.get()
   email = t2.get()
   phone = t3.get()
   
   qry = "insert into student values(%s,%s,%s,%s)"
   val = (0,name,email,phone)
   cursor.execute(qry,val)
   con.commit()
   print("Data inserted")
   
   t1.delete(0,END)
   t2.delete(0,END)
   t3.delete(0,END)

# b = Button(root,text="Submit")
# b.pack(side=LEFT)
# b1 = Button(root,text="Submit")
# b1.pack(side=RIGHT)
# b2 = Button(root,text="Submit")
# b2.pack(side=TOP)
# b3 = Button(root,text="Submit")
# b3.pack(side=BOTTOM)


# l1 = Label(root, text="Username")
# l1.grid(row=1,column=1)

# l2 = Label(root, text="Email")
# l2.grid(row=2,column=1)

# l3 = Label(root, text="Phone")
# l3.grid(row=3,column=1)


# t1 = Entry(root)
# t1.grid(row=1,column=2)
# t2 = Entry(root)
# t2.grid(row=2,column=2)
# t3 = Entry(root)
# t3.grid(row=3,column=2)

# b = Button(root, text="submit")
# b.grid(row=4,column=2)



l1 = Label(root, text="Username")
l1.place(x=100,y=100)

l2 = Label(root, text="Email")
l2.place(x=100,y=150)

l3 = Label(root, text="Phone")
l3.place(x=100,y=200)


t1 = Entry(root)
t1.place(x=170,y=100)
t2 = Entry(root)
t2.place(x=170,y=150)
t3 = Entry(root)
t3.place(x=170, y=200)

b = Button(root, text="submit", width=15,command=get_data)
b.place(x=170, y=250)

    



root.mainloop()
