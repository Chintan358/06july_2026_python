import mysql.connector as sql

con = sql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="6july_python"
)

cursor = con.cursor()

# print(con.is_connected())
# con._execute_query("create database 6july_python")

# qry = "create table student(id int,name varchar(20),email varchar(50))"
# cursor.execute(qry)

# qry = "insert into student values(1,'Meet','meet@gmial.com')"
# cursor.execute(qry)
# con.commit()

id = input("enter id : ")
name = input("enter name : ")
email = input("enter email : ")

qry = "insert into student values(%s,%s,%s)"
val = (id,name,email)
cursor.execute(qry,val)
con.commit()