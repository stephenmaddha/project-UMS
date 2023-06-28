import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='stephen@16'
)
cur=conn.cursor()
class updated:
    def departmentupdate(x,colname,newvalue,oldvalue):
        cur.execute(f"update department set {colname}='{newvalue}' where {colname}='{oldvalue}'")
        conn.commit()
    def courseupdate(x,colname,newvalue,oldvalue):
        cur.execute(f"update course set {colname}='{newvalue}' where {colname}='{oldvalue}'")
        conn.commit()

    def facultyupdate(x,colname,newvalue,oldvalue):
        cur.execute(f"update faculty set {colname}='{newvalue}' where {colname}='{oldvalue}'")
        conn.commit()

    def studentupdate(x,colname,newvalue,oldvalue):
        cur.execute(f"update student set {colname}='{newvalue}' where {colname}='{oldvalue}'")
        conn.commit()


