import mysql.connector as myconn #! it mysql.connector not mysql_connector
#! we alias it as myconn
mydb = myconn.connect(
    host = "localhost", #! host
    user = "root", #! username
    password = "root", #! password
    database = "pythonMysql" #! database name
)

mycursor = mydb.cursor() #! cursor is an object

#mycursor.execute("insert into student(id,name) values(%s,%s)",(2,"virat")) #! insert values a single tuple

db_insert = "insert into student(id,name) values(%s,%s)"
db_list = [(3,"rohit"),(4,"rahul"),(5,"suresh")]

mycursor.executemany(db_insert,db_list)
print(mycursor.rowcount,"values inserted") #! it will print values inserted
mydb.commit() #! it will commit the changes