
import mysql.connector

if __name__ == '__main__':
    
    
    connection=mysql.connector.connect(
        user="root",
        password="Kru@123",
        host="localhost",
        database="stockbuddy"
    )
    
    cursor=connection.cursor()   
    query="SELECT * FROM `user data`"
    cursor.execute(query)
    results=cursor.fetchall()

    for data in results:
        print(data)
        
