import os
import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt
import mysql.connector as msql
from mysql.connector import Error
import csv


irisData = pd.read_csv('https://raw.githubusercontent.com/Muhd-Shahid/Learn-Python-Data-Access/main/iris.csv',index_col=False)
irisData.head()
df = irisData
df.head()

conn_params_dic = {
    "host"      : "localhost",
    "database"  : "irisdb",
    "user"      : "root",
    "password"  : "passme123@#$"
}


# Define a connect function for MySQL database server
def connect(conn_params_dic):
    conn = None
    try:
        print('Connecting to the MySQL...........')
        conn = msql.connect(**conn_params_dic)
        print("Connection successfully..................")

    except Error as err:
        print("Error while connecting to MySQL", err)
        # set the connection to 'None' in case of error
        conn = None
    return conn
connect_alchemy = "mysql+pymysql://%s:%s@%s/%s" % (
    conn_params_dic['user'],
    conn_params_dic['password'],
    conn_params_dic['host'],
    conn_params_dic['database']
)

def using_alchemy():
    try:
        print('Connecting to the MySQL...........')
        engine = create_engine(connect_alchemy)
        print("Connection successfully..................")
    except Error as err:
        print("Error while connecting to MySQL", err)
        # set the connection to 'None' in case of error
        engine = None
    return engine

def create_table(engine):
    try:
        # Dropping table iris if exists
        engine.execute("DROP TABLE IF EXISTS iris;")
        sql = '''CREATE TABLE iris(
        sepal_length DECIMAL(2,1) NOT NULL, 
        sepal_width DECIMAL(2,1) NOT NULL, 
        petal_length DECIMAL(2,1) NOT NULL, 
        petal_width DECIMAL(2,1),
        species CHAR(11) NOT NULL
        )'''
        # Creating a table
        engine.execute(sql);
        print("iris table is created successfully................")
    except Error as err:
        print("Error while connecting to MySQL", err)
        # set the connection to 'None' in case of error
        conn = None
















#need modification check : https://python.plainenglish.io/how-to-import-a-csv-file-into-a-mysql-database-using-python-script-791b051c5c33