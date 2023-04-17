import mysql.connector

dataBase = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    passwd = '#01EDMinmyblood'
)

# prepare a cursor object
cursorObj = dataBase.cursor()

# Create a database
cursorObj.execute("CREATE DATABASE IF NOT EXISTS myDatabase")

print ('All Done!')