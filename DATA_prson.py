import mysql.connector as mysql
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')

    mySql_Create_Table_Query = """CREATE TABLE Persons ( 
                             Id int(11) NOT NULL,
                             Firstname varchar(250) NOT NULL,
                             Lastname varchar(250) NOT NULL,
                             Slot_date Date NOT NULL,
                             PRIMARY KEY (Id)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Person Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")