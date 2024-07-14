import sqlite3

class view_data:
    def __init__(self):
        self.con = sqlite3.connect('sms.db')
        self.cur = self.con.cursor()

    def viewstudent(self):
        self.cur.execute('select * from student')
        rows = self.cur.fetchall()
        print("==STUDENT DATA==")
        for row in rows:
            print(row)
        
    def viewcourse(self):
        self.cur.execute('select * from course')
        rows = self.cur.fetchall()
        print("==COURSE DATA==")
        for row in rows:
            print(row)

    def viewtransaction(self):
        self.cur.execute('select * from transcation')
        rows = self.cur.fetchall()
        print("==TRANSCATION DATA==")
        for row in rows:
            print(row)
