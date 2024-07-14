import sqlite3

class updatedata:
    def __init__(self):
        self.con = sqlite3.connect('sms.db')
        self.cur = self.con.cursor()

    def update_student(self, sid, name=None, email=None, city=None):
            if name:
                self.cur.execute('UPDATE student SET name = ? WHERE sid = ?', (name, sid))
            if email:
                self.cur.execute('UPDATE student SET email = ? WHERE sid = ?', (email, sid))
            if city:
                self.cur.execute('UPDATE student SET city = ? WHERE sid = ?', (city, sid))
            self.con.commit()
            print("Student data updated successfully")
            

    def update_course(self, cid, cname=None, sid=None, price=None):
            if cname:
                self.cur.execute('UPDATE course SET cname = ? WHERE cid = ?', (cname, cid))
            if sid:
                self.cur.execute('UPDATE course SET sid = ? WHERE cid = ?', (sid, cid))
            if price:
                self.cur.execute('UPDATE course SET price = ? WHERE cid = ?', (price, cid))
            self.con.commit()
            print("Course data updated successfully")
           

    def update_transaction(self, tid, cid=None, sid=None, method=None):
            if cid:
                self.cur.execute('UPDATE transaction SET cid = ? WHERE tid = ?', (cid, tid))
            if sid:
                self.cur.execute('UPDATE transaction SET sid = ? WHERE tid = ?', (sid, tid))
            if method:
                self.cur.execute('UPDATE transaction SET method = ? WHERE tid = ?', (method, tid))
            self.con.commit()
            print("Transaction data updated successfully")
            