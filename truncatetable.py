import mysql.connector as myconn #! it mysql.connector not mysql_connector
#! we alias it as myconn
mydb = myconn.connect(
    host = "localhost", #! host
    user = "root", #! username
    password = "root", #! password
    database = "pythonMysql" #! database name
)

mycursor = mydb.cursor() #! cursor is an object
db_truncate = "truncate table student"

mycursor.execute(db_truncate)

mydb.commit() #! it will commit the changes
print(mycursor.rowcount,"values deleted")