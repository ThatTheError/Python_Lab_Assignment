import mysql.connector as c

conn = c.connect(host='localhost',user='root',passwd='',database='Python_Database')
cursor = conn.cursor(buffered = True)
createQuery ="select * from student;"
try:
    cursor.execute(createQuery)
    co = cursor.rowcount
    print("Student Database has ",co," No. of records")
    no = int(input("how many record you want to fetch?\n"))
    data = cursor.fetchmany(no)
    print("FETCHED DATA = ",data)
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