import sqlite3

con = sqlite3.connect("data.db")

# qry = "create table student(id int,name varchar(20),email varchar(50))"

# qry = "insert into student values(3,'Meet','meet@gmail.com')"

# qry = "update student set name='xyz' where id=4"

# qry = "delete from student where id = 4"

# con.execute(qry) 
# con.commit()

data = con.execute("select * from student")
for i in data.fetchmany(2):
    print(i)