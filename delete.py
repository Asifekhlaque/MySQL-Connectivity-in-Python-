import mysql.connector as myconn #! it mysql.connector not mysql_connector
#! we alias it as myconn
mydb = myconn.connect(
    host = "localhost", #! host
    user = "root", #! username
    password = "root", #! password
    database = "pythonMysql" #! database name
)

mycursor = mydb.cursor() #! cursor is an object

db_delete = "delete from student where id = %s"
dbvalues = (4,)

mycursor.execute(db_delete,dbvalues)

mydb.commit() #! it will commit the changes
print(mycursor.rowcount,"values deleted")