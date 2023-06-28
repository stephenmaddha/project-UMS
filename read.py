import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='stephen@16'
)
cur=conn.cursor()

class readed:
    def departmentread(x,id):
        cur.execute(f"select * from department where department_id={id}")
        print(cur.fetchall())
    def courseread(x,id):
        cur.execute(f"select * from course where course_id={id}")
        print(cur.fetchall())
    def facultyread(x,id):
        cur.execute(f"select * from faculty where faculty_id={id}")
        print(cur.fetchall())
    def studentread(x,id):
        cur.execute(f"select * from student where student_id={id}")
        print(cur.fetchall())
    