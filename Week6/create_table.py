import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Tushariccs"
)
# print(mydb)

myscusor = mydb.cursor()
myscusor.execute("Create Database if not exists test1")
myscusor.execute("CREATE TABLE if not exists test1.test_table(c1 int PRIMARY KEY,c2 VARCHAR(90),c3 DATE,c4 FLOAT,c5 varchar(30))")
mydb.close()