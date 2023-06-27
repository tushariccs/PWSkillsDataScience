import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Tushariccs"
)
# print(mydb)

myscusor = mydb.cursor()
myscusor.execute("select * from test1.test_table")
for i in myscusor.fetchall():
    print(i)