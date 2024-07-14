import sqlite3

class insertdata:
    def __init__(self):
        self.con = sqlite3.connect('sms.db')
        self.cur = self.con.cursor()

    def insertstudent(self,sid,name,email,city):
        self.cur.execute(f'''
                         insert into student values
                         (
                         {sid},
                         "{name}",
                         "{email}",
                         "{city}"
                         )
                         ''')
        self.con.commit()
        print("Data Added Success")

    def insertcourse(self,cid,cname,sid,price):
        self.cur.execute(f'''
                         insert into transcation values
                         (
                         {cid},
                         "{cname}",
                         {sid},
                         {price}
                         )
                         ''')
        self.con.commit()
        print("Success")

    def inserttranscation(self,tid,cid,sid,method):
        self.cur.execute(f'''
                         insert into transcation values
                         (
                         {tid},
                         {cid},
                         {sid},
                         "{method}"
                         )
                         ''')
        self.con.commit()
        print("Added success")
   
    