import mysql.connector as c

conn = c.connect(host='localhost',user='root',passwd='',database='Python_Database')
cursor = conn.cursor(buffered = True)
createQuery ="select * from student;"
try:
    cursor.execute(createQuery)
    data = cursor.fetchall()
    print("Total no. of data = ",cursor.rowcount)
    print("FETCH ALL DATA = ",data)
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