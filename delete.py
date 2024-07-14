import sqlite3

class deletedata:
    def __init__(self):
        self.con = sqlite3.connect('sms.db')
        self.cur = self.con.cursor()

    def delete_from_student(self,sid):
        self.cur.execute(f'''
                         delete from student where sid={sid}
                        
                         ''')
        self.con.commit()
        print("Deleted  Success")

    def delete_from_course(self,cid):
       self.cur.execute(f"delete from course where cid={cid}")
       self.con.commit()
       print("Deleted  Success")
        
    def delete_from_transcation(self,tid):
        self.cur.execute(f'''
                         delete from transcation where tid={tid}
                        
                         ''')
        self.con.commit()
        print("Deleted  Success")

    