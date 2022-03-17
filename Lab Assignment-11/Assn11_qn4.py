import mysql.connector as c

conn = c.connect(host='localhost',user='root',passwd='',database='Python_Database')
cursor = conn.cursor()
createQuery ="delete from emp_005 where empno%2=0;"
print('Row Deleted ..')
try:
    cursor.execute(createQuery)
    conn.commit()
except Exception as ex:
    print(ex)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

















"""
import mysql.connector as c
conn = c.connect(host='localhost',user='root',passwd='',database='Python_Database')
cursor = conn.cursor(buffered = True)
createQuery ="drop table if exists emp_005;"
try:
    cursor.execute(createQuery)
    conn.rollback()
except Exception as ex:
    if conn!=None:
        conn.rollback()
        print("There is some problem")
        print(ex)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
"""