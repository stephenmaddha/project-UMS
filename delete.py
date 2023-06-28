import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='stephen@16'
)
cur=conn.cursor()
class deleted:
    def departmentdelete(x,id):
        cur.execute(f"delete from department where department_id={id} ")
        conn.commit()
    def coursedelete(x,id):
        cur.execute(f"delete from course where course_id={id} ")
        conn.commit()
    def facultydelete(x,id):
        cur.execute(f"delete from faculty where faculty_id={id} ")
        conn.commit()
    def studentdelete(x,id):
        cur.execute(f"delete from student where student_id={id} ")
        conn.commit()

        