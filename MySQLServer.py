import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="M36966313m!"
)

mycursor = mydb.cursor()

sql = "CREATE DATABASE IF NOT EXISTS alx_book_store"
try:
    mycursor.execute(sql)
except mysql.connector.Error as err:
    print(f"Error: {err}")
else:  
    print("Database 'alx_book_store' created successfully!")
finally:
    mycursor.close()
    mydb.close()
