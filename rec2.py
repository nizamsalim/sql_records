import mysql.connector as ms


def initDatabase():
    sqlConn = ms.connect(
        host="localhost", user="root", password="nizam123")

    if sqlConn.is_connected() == False:
        print("Connection failed")
        return None
    else:
        db = sqlConn.cursor()
        db.execute("CREATE DATABASE IF NOT EXISTS sales")
        db.execute("USE sales")
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS item(
                itemcode INT(3),
                itemname VARCHAR(25),
                qty INT(4),
                cost INT(5),
                supplier VARCHAR(25)
            )
            """
        )
        return db, sqlConn


def closeDatabase():
    db.close()
    sqlConn.close()


def addRecord(row):
    db.execute(f"INSERT INTO item VALUES{row}")
    sqlConn.commit()


def deleteRecord(cde):
    db.execute(f"DELETE FROM item WHERE itemcode={cde}")
    sqlConn.commit()


def updateRecord(code, newName, newSupplier, newQty, newCost):
    db.execute(
        f"UPDATE item SET itemname='{newName}',supplier='{newSupplier}',qty={newQty},cost={newCost} WHERE itemcode={code}"
    )
    sqlConn.commit()


def displayAllRecords():
    db.execute("SELECT * FROM item")
    data = db.fetchall()
    for doctor in data:
        print(doctor)


# main segment
res = initDatabase()
if res == None:
    exit()
db, sqlConn = res

while True:
    print(
        "1. Add Record\n2. Delete Record\n3. Update Record\n4. Display all records\n5. Exit\n"
    )
    choice = int(input("Enter option (1-4) : "))
    if choice == 1:
        code = int(input("Itemcode : "))
        name = input("Item name : ")
        qty = int(input("Item quantity : "))
        cost = int(input("Item cost : "))
        supplier = input("Supplier : ")
        addRecord((code, name, qty, cost, supplier))

    elif choice == 2:
        code = int(input("Id to be deleted : "))
        deleteRecord(code)

    elif choice == 3:
        code = int(input("Id to be updated : "))
        name = input("Item name(updated) : ")
        qty = int(input("Item quantity(updated) : "))
        cost = int(input("Item cost(updated) : "))
        supplier = input("Supplier(updated) : ")
        updateRecord(code, name, supplier, qty, cost)

    elif choice == 4:
        displayAllRecords()

    elif choice == 5:
        break
    else:
        print("Invalid input")

    repeat = input("Repeat(Y/N)? : ")
    if repeat in "nN":
        break
    print("--------------------------------------------")
closeDatabase()
