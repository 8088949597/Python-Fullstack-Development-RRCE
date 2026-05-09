import pymysql

connection = None

try:
    connection = pymysql.connect(
        host="localhost",
        port=5000,  
        user="root",
        password="Kavya@8088",
        database="mydb"
    )

    print("Connected successfully!")

    cursor = connection.cursor()

    
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    print("Tables in mydb:")
    for table in tables:
        print(table)

    
    cursor.execute("SELECT * FROM student   ")
    rows = cursor.fetchall()

    print("Data inside table:")
    for row in rows:
        print(row)

except Exception as e:
    print("Error:", e)

finally:
    if connection:
        connection.close()
        print("Connection closed.")