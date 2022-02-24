import mysql.connector as c

conn = c.connect(host='localhost',user='root',passwd='',database='Python_Database')
cursor = conn.cursor()
try:
    cursor.execute("insert into emp_005(empno,first_name,last_name,sal,dept_no)values(1,'Abagail','Twitty',6882.27,20);")
    cursor.execute("insert into emp_005(empno,first_name,last_name,sal,dept_no)values(2,'Lurlene','Lineham',2713.96,20);")
    cursor.execute("insert into emp_005(empno,first_name,last_name,sal,dept_no)values(3,'Barrie','Gathercoal',1168.5,20);")
    cursor.execute("insert into emp_005(empno,first_name,last_name,sal,dept_no)values(4,'Dorian','Cossor',8071.84,40);")
    cursor.execute("insert into emp_005(empno,first_name,last_name,sal,dept_no)values(5,'Emilee','Villaron',3421.77,30);")
    cursor.execute("insert into emp_005(empno,first_name,last_name,sal,dept_no)values(6,'Dasha','Tapenden',2556.74,30);")
    cursor.execute("insert into emp_005(empno,first_name,last_name,sal,dept_no)values(7,'Tamma','Timmes',3410.98,40);")
    cursor.execute("insert into emp_005(empno,first_name,last_name,sal,dept_no)values(8,'Lenci','Bruno',9079.36,40);")
    cursor.execute("insert into emp_005(empno,first_name,last_name,sal,dept_no)values(9,'Fawnia','Insull',4594.5,30);")
    cursor.execute("insert into emp_005(empno,first_name,last_name,sal,dept_no)values(10,'Carmine','Ricardot',2696.09,30);")
except Exception as ex:
    print(ex)
finally:
    conn.commit()
    if cursor:
        cursor.close()
    if conn:
        conn.close()