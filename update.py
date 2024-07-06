import mysql.connector as myconn #! it mysql.connector not mysql_connector
#! we alias it as myconn
mydb = myconn.connect(
    host = "localhost", #! host
    user = "root", #! username
    password = "root", #! password
    database = "pythonMysql" #! database name
)

mycursor = mydb.cursor() #! cursor is an object
db_update = "update student set name = %s where id = %s"
dbvalues = ("shivam",5)

mycursor.execute(db_update,dbvalues)

mydb.commit() #! it will commit the changes