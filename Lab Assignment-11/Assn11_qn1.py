import mysql.connector as c

conn = c.connect(host='localhost',user='root',passwd='',database='Python_Database')
cursor = conn.cursor()
createQuery ="""
create table emp_005(
    empno integer(3),
    first_name varchar(12),
    last_name varchar(12),
    sal float(6,2),
    dept_no integer(2)
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