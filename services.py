import requests
import json
import time
import os
from dotenv import load_dotenv
import mysql.connector

class Table:
    def table_1():
        mydb = mysql.connector.connect(
            host=os.getenv('DB_URL'),
            port=os.getenv('DB_PORT'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )

        dbcursor = mydb.cursor()

        dbcursor.execute("SELECT * FROM tabla")

        dbtable = dbcursor.fetchall()

        return dbtable
    
    def table_2():
        mydb = mysql.connector.connect(
            host=os.getenv('DB_URL'),
            port=os.getenv('DB_PORT'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        
        dbcursor = mydb.cursor()

        dbcursor.execute("SELECT * FROM tabla2")

        dbtable = dbcursor.fetchall()

        return dbtable
