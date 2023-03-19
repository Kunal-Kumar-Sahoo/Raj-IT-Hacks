import mysql.connector

connection = mysql.connector.connect(
    host='localhost', user='kunal', passwd='6anmol',
    database='RAJITHACKS', auth_plugin='mysql_native_password'
)

cursor = connection.cursor()

