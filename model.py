import mysql.connector

class Model:
    def connect(self):
        return mysql.connector.connect(
            host = "localhost", 
            user = "root", 
            password = "", 
            database = "rwt_dojo")

    def getCount(self):
        con = Model.connect(self)
        cur = con.cursor()
        cur.execute("SELECT COUNT(id) AS total FROM course; ")
        total_course = cur.fetchone()
        cur.execute("SELECT COUNT(id) AS total FROM event; ")
        total_event = cur.fetchone()
        cur.execute("SELECT COUNT(id) AS total FROM sensei; ")
        total_sensei = cur.fetchone()
        cur.execute("SELECT COUNT(id) AS total FROM student; ")
        total_student = cur.fetchone()
        data = [total_course, total_event, total_sensei, total_student]
        return data

    def login(self, uname):
        con = Model.connect(self)
        cur = con.cursor()
        query = "SELECT id, username, password FROM user WHERE username=%s"
        cur.execute(query, (uname, ))
        row = cur.fetchone()
        return row
        
    def getcourseprice(self):
        con = Model.connect(self)
        cur = con.cursor()
        cur.execute("select * from course")
        row = cur.fetchall()
        return row