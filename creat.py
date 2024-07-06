import mysql.connector as myconn #! it mysql.connector not mysql_connector
#! we alias it as myconn
mydb = myconn.connect(
    host = "localhost", #! host
    user = "root", #! username
    password = "root", #! password
    database = "pythonMysql" #! database name
)
print(mydb,"database connected") #! it will print database connected
mycursor = mydb.cursor() #! cursor is an object
mycursor.execute("create database pythonMysql") #* create database
print("database created") #* database created