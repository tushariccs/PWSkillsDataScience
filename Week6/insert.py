import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Tushariccs"
)
# print(mydb)

myscusor = mydb.cursor()
myscusor.execute("INSERT INTO test1.test_table values(1,'Tushar','2002-2-25',34.12,'Hii')")
mydb.commit()
mydb.close()