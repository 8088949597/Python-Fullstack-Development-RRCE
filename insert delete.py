import pymysql

connection = None

try:
    connection = pymysql.connect(
        host="localhost",
        port=5000,  # Usually 3306 unless changed
        user="root",
        password="Kavya@8088",
        database="mydb"
    )

    print("Connected successfully!")

    cursor = connection.cursor()

    # INSERT
    cursor.execute(
        "INSERT INTO student (RNo, name, city) VALUES (%s, %s, %s)",
        (3, "Ravi", "Hyderabad")
    )
    connection.commit()
    print("Inserted successfully!")

    # DELETE
    cursor.execute(
        "DELETE FROM student WHERE RNo = %s",
        (3,)
    )
    connection.commit()
    print("Deleted successfully!")

except Exception as e:
    print("Error:", e)

finally:
    if connection:
        connection.close()
        print("Connection closed.")