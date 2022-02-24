import mysql.connector as c

conn = c.connect(host='localhost',user='root',passwd='',database='Python_Database')
cursor = conn.cursor(buffered = True)
createQuery ="update emp_005 set sal=sal+sal*0.10 where sal>5000;"
try:
    cursor.execute("select * from emp_005;")
    print("Before Updation = ",cursor.fetchall())
    cursor.execute(createQuery)
    conn.commit()
    print("Row Updated")
    cursor.execute("select * from emp_005;")
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