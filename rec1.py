import mysql.connector as ms


def initDatabase():
    sqlConn = ms.connect(
        host="localhost", user="root", password="nizam123", database="hospital"
    )

    if sqlConn.is_connected() == False:
        print("Connection failed")
        return None
    else:
        return sqlConn.cursor(), sqlConn


def closeDatabase():
    db.close()
    sqlConn.close()


def addRecord(row):
    db.execute(f"INSERT INTO doctor VALUES{row}")
    sqlConn.commit()


def deleteRecord(d_id):
    db.execute(f"DELETE FROM doctor WHERE docid={d_id}")
    sqlConn.commit()


def updateRecord(d_id, newName, newDept, newSalary, newExp):
    db.execute(
        f"UPDATE doctor SET docname='{newName}',dept='{newDept}',salary='{newSalary}',yrs_exp='{newExp}' WHERE docid={d_id}"
    )
    sqlConn.commit()


def displayAllRecords():
    db.execute("SELECT * FROM doctor")
    data = db.fetchall()
    for doctor in data:
        print(doctor)


# main segment
db, sqlConn = initDatabase()
if db == None:
    exit()

while True:
    print(
        "1. Add Record\n2. Delete Record\n3. Update Record\n4. Display all records\n5. Exit\n"
    )
    choice = int(input("Enter option (1-4) : "))
    print()
    if choice == 1:
        d_id = int(input("Doctor id : "))
        name = input("Doctor name : ")
        dept = input("Department : ")
        sal = int(input("Salary : "))
        exp = int(input("Years of experience : "))
        addRecord((d_id, name, dept, sal, exp))
        print()
    elif choice == 2:
        d_id = int(input("Id to be deleted :"))
        deleteRecord(d_id)
        print()
    elif choice == 3:
        d_id = int(input("Id to be updated : "))
        name = input("Doctor name(updated) : ")
        dept = input("Department(updated) : ")
        sal = int(input("Salary(updated) : "))
        exp = int(input("Years of experience(updated) : "))
        updateRecord(d_id, name, dept, sal, exp)
        print()
    elif choice == 4:
        displayAllRecords()
        print()
    elif choice == 5:
        exit()
    else:
        print("Invalid input")
        print()
    repeat = input("Repeat(Y/N)? : ")
    if repeat in "nN":
        break
    print("--------------------------------------------")
closeDatabase()
