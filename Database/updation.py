import mysql.connector as c

conn = c.connect(host='localhost',user='root',passwd='',database='Python_Database')
cursor = conn.cursor(buffered = True)
createQuery ="update student set name = 'V Gopal' where roll=005;"
try:
    cursor.execute("select * from student;")
    print("Before Updation = ",cursor.fetchall())
    cursor.execute(createQuery)
    conn.commit()
    print("Row Updated")
    cursor.execute("select * from student;")
    print("After Updation = ",cursor.fetchall())
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