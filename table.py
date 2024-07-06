import mysql.connector as myconn #! it mysql.connector not mysql_connector
#! we alias it as myconn
mydb = myconn.connect(
    host = "localhost", #! host
    user = "root", #! username
    password = "root", #! password
    database = "pythonMysql" #! database name
)

mycursor = mydb.cursor() #! cursor is an object
mycursor.execute("create table student(id int,name varchar(20))") #! create table
print("table created") #! table created
mycursor.execute("show tables") #! show tables
for i in mycursor: #! for loop for table name
    print(i)