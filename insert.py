import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='stephen@16'
)
cur=conn.cursor()
class inserted:
    def departmentinsert(x,did,dname):
        cur.execute(f"insert into department values({did},'{dname}')")
        conn.commit()
    def courseinsert(x,cid,cname,cfee,cdur):
        cur.execute(f"insert into course values({cid},'{cname}',{cfee},{cdur})")
        conn.commit()
    def facultyinsert(x,fid,fname,fdepartmentid,fsalary,fcourseid):
        cur.execute(f"insert into faculty values({fid},'{fname}',{fdepartmentid},{fsalary},{fcourseid})")
        conn.commit()
    def studentinsert(x,sid,sname,scourseid,sdepartmentid):
        cur.execute(f"insert into student values({sid},'{sname}',{scourseid},{sdepartmentid})")
        conn.commit()