from logging import exception
import mysql.connector as c
conn = c.connect(host='localhost',user='root',passwd='',database='Python_Database')
cursor = conn.cursor()
createQuery ="""
create table student(
    name varchar(10),
    roll integer(3),
    id integer primary key
);
"""
try:
    cursor.execute(createQuery)
    print("Table Created Sucessfully...")
except Exception as ex:
    print(ex)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()