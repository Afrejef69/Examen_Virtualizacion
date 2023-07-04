import requests
import json
import time
import os
from dotenv import load_dotenv
import mysql.connector

class Table:
    def table_1():
        mydb = mysql.connector.connect(
            host=os.getenv('DATABASE_URL'),
            port=os.getenv('DATABASE_PORT'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD'),
            database=os.getenv('DATABASE_NAME')
        )

        dbcursor = mydb.cursor()

        dbcursor.execute("SELECT * FROM personaje")

        dbtable = dbcursor.fetchall()
        return dbtable

    def table_2():
        mydb2 = mysql.connector.connect(
            host=os.getenv('DATABASE_URL'),
            port=os.getenv('DATABASE_PORT'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD'),
            database=os.getenv('DATABASE_NAME')
        )

        dbcursor = mydb2.cursor()

        dbcursor.execute("SELECT * FROM poder")

        dbtable = dbcursor.fetchall()
        return dbtable
