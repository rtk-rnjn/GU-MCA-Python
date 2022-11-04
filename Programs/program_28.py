# Python program to connect to MySQL database

import mysql.connector  # type: ignore

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="password", database="mydatabase"
)

# Create a cursor
mycursor = mydb.cursor()

# Execute a query
mycursor.execute("SELECT * FROM customers")

# Fetch all rows
myresult = mycursor.fetchall()

# Print all rows
for x in myresult:
    print(x)
