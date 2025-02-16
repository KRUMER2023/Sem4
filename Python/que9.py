"""
1 step:
we need to install a lib call mysql-connector-python
pip install mysql-connector-python

2 step:

import sql to your file
import mysql.connector

create connection with your database:
params which is required for creation the connection:
    1. user  -->> root
    2. password ---->>; root
    3. host--->> localhost
    4. database_name--> db name

    once connection is built then we can writer the query with
    cursor object

"""

import mysql.connector

if __name__ == '__main__':
    
    # step 1
    connection=mysql.connector.connect(
        user="root",
        password="root",
        host="localhost",
        database="bank_db"
    )
    
    # step 2
    cursor=connection.cursor()   # through this cursor object we are pointing to the database tables

    #step 3
    query="select * from accountdetails"

    #step 4
    cursor.execute(query)
    # step 5
    results=cursor.fetchall()

    for data in results:
        print(data)