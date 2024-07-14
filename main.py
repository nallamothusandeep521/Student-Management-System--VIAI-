from insert import insertdata
from delete import deletedata
from read import view_data
from update import updatedata

#creating objects
obj = insertdata()
view = view_data()
delete = deletedata()
upd = updatedata()

print("=========Student Management System==============")
print("Slect\n 1.Insert \n 2.Delete \n 3.Read \n 4.Update")
num = int(input("Enter your Choice"))

if num == 1:
    print("Choose \n 1.student: \n 2.Course \n 3.transcation")
    n = int(input("Enter your option: "))

    if n == 1:
        sid  = int(input("Enter id: "))
        name = input("Enter name:")
        email = input("Enter email:")
        city = input("Enter city: ")
        obj.insertstudent(sid,name,email,city)

    elif n == 2:
        cid  = int(input("Enter id: "))
        cname = input("Enter course name:")
        sid = int(input("Enter student id:"))
        price = int(input("Enter price: "))
        obj.insertcourse(cid,cname,sid,price)

    elif n == 3:
        tid = int(input("Enter Transcation ID: "))
        cid  = int(input("Enter Course Id: "))
        sid = int(input("Enter student id: "))
        method = input("Enter Method of Payment: ")
        obj.inserttranscation(tid,cid,sid,method)

elif num == 3:
    print("Choose \n 1.student: \n 2.Course \n 3.transcation \n 4.View All Tables Data")
    n = int(input("Enter your option: "))

    if n == 1:
        view.viewstudent()

    elif n == 2:
        view.viewcourse()
    
    elif n == 3:
         view.viewtransaction()

    elif n==4:
        print("Student Data")
        view.viewstudent()
        print("Course Data")
        view.viewcourse()
        print("Transcation Data")
        view.viewtransaction()

elif num == 2:
    print("Choose \n 1.student: \n 2.Course \n 3.transcation")
    n = int(input("Enter your option: "))

    if n==1:
        sid = int(input("Enter student ID to delete: "))
        delete.delete_from_student(sid)
    elif n==2:
        cid = int(input("Enter Course ID to delete: "))
        delete.delete_from_course()
    elif n ==3:
        tid = int(input("Enter Transcation ID to delete: "))
        delete.delete_from_transcation()

elif num == 4:
    print("Choose\n 1. Student\n 2. Course\n 3. Transaction")
    n = int(input("Enter your option: "))

    if n == 1:
        sid = int(input("Enter student ID to update: "))
        name = input("Enter new name (leave blank if no change): ")
        email = input("Enter new email (leave blank if no change): ")
        city = input("Enter new city (leave blank if no change): ")
        upd.update_student(sid, name if name else None, email if email else None, city if city else None)

    elif n == 2:
        cid = int(input("Enter course ID to update: "))
        cname = input("Enter new course name (leave blank if no change): ")
        sid = input("Enter new student ID (leave blank if no change): ")
        price = input("Enter new price (leave blank if no change): ")
        upd.update_course(cid, cname if cname else None, sid if sid else None, price if price else None)

    elif n == 3:
        tid = int(input("Enter transaction ID to update: "))
        cid = input("Enter new course ID (leave blank if no change): ")
        sid = input("Enter new student ID (leave blank if no change): ")
        method = input("Enter new method (leave blank if no change): ")
        upd.update_transaction(tid, cid if cid else None, sid if sid else None, method if method else None)
