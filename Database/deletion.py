import mysql.connector as c

conn = c.connect(host='localhost',user='root',passwd='',database='Python_Database')
cursor = conn.cursor()
createQuery ="delete from student where id>2;"
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