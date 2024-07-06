import mysql.connector as myconn #! it mysql.connector not mysql_connector
#! we alias it as myconn
mydb = myconn.connect(
    host = "localhost", #! host
    user = "root", #! username
    password = "root", #! password
    database = "pythonMysql" #! database name
)

mycursor = mydb.cursor() #! cursor is an object
mycursor.execute("select * from student") #! select all from student

for i in mycursor.fetchall(): #! for loop for all values it a better way
    print(i)

#print(mycursor.fetchall()) #! fetchall is used to fetch all values