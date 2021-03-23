import pandas as pd

import mysql.connector as msql
from mysql.connector import Error

irisData = pd.read_csv('iris.csv',index_col=False)
irisData.head()


try:
    conn = msql.connect(host='localhost', user='root',
                        password='passme123@#$')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE irisDB")
        print("irisDB database is created")
except Error as e:
    print("Error while connecting to MySQL", e)


try:
    conn = msql.connect(host='localhost',
                           database='irisDB', user='root',
                           password='sql@123')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS iris;')
        print('Creating table....')
        cursor.execute("CREATE TABLE iris (sepal_length FLOAT(2,1)
                        NOT NULL, sepal_width FLOAT(2,1) NOT NULL,
                        petal_length FLOAT(2,1) NOT NULL,
                        petal_width FLOAT(2,1),species CHAR(11)NOT
                        NULL)")
        print("iris table is created....")
        for i,row in irisData.iterrows():
            sql = "INSERT INTO irisdb.iris VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not autocommitted by default, so we
             must commit to save our changes
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)


#need modification check : https://python.plainenglish.io/how-to-import-a-csv-file-into-a-mysql-database-using-python-script-791b051c5c33