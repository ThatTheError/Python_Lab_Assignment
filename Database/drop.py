import mysql.connector as c

conn = c.connect(host='localhost',user='root',passwd='',database='Python_Database')
cursor = conn.cursor(buffered = True)
createQuery ="drop table if exists student;"
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