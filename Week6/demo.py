import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Tushariccs"
)
print(mydb)

myscusor = mydb.cursor()
myscusor.execute("SHOW DATABASES")
# print(a)
for x in myscusor:
    print(x)