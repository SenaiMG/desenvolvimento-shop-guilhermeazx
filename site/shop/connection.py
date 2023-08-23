import mysql.connector

cnx = mysql.connector.connect(user='root', password = '', host = 'localhost')
cnx.close()

mycursor = cnx.cursor
mycursor.execute('CREATE DATABASE mydatabase')