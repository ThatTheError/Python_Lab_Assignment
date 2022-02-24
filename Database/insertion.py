import mysql.connector as c

conn = c.connect(host='localhost',user='root',passwd='',database='Python_Database')
cursor = conn.cursor()
try:
    cursor.execute("insert into student(name,roll,id)values('Gopal',005,1);")
    cursor.execute("insert into student(name,roll,id)values('Ram',006,2);")
    cursor.execute("insert into student(name,roll,id)values('Hari',006,3);")
    cursor.execute("insert into student(name,roll,id)values('Siba',008,4);")
    cursor.execute("insert into student(name,roll,id)values('Madan',009,5);")
    cursor.execute("insert into student(name,roll,id)values('Sudam',012,6);")
except Exception as ex:
    print(ex)
finally:
    conn.commit()
    if cursor:
        cursor.close()
    if conn:
        conn.close()