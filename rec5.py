import mysql.connector as ms


def initDatabase():
    sqlConn = ms.connect(host="localhost", user="root", password="nizam123")

    if sqlConn.is_connected() == False:
        print("Connection failed")
        return None
    else:
        db = sqlConn.cursor()
        db.execute("CREATE DATABASE IF NOT EXISTS sales")
        db.execute("USE sales")
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS item2(
                itemcode INT(3),
                itemname VARCHAR(25),
                qty INT(4),
                cost INT(5),
                supplier VARCHAR(25),
                date_supply VARCHAR(10)
            )
            """
        )
        return db, sqlConn


def closeDatabase():
    db.close()
    sqlConn.close()


def addInitialRecords():
    # db.execute("SELECT COUNT(*) FROM marks")
    # if db.fetchall()[0][0] != 0:
    #     return
    # itemcode, itemname, qty, cost, supplier, date_supply.
    n = int(input("Number of records to add : "))
    k = 0
    for i in range(n):
        itCode = int(input("Item code : "))
        itName = input("Item name : ")
        qty = int(input("Quantity : "))
        cost = int(input("Cost : "))
        supp = input("Supplier name : ")
        date = input("Date of supply(yyyy-mm-dd) : ")
        db.execute(
            f"INSERT INTO item2 VALUES({itCode},'{itName}',{qty},{cost},'{supp}','{date}')")
        k = 1
    if k == 1:
        sqlConn.commit()


def getItemsWithCostMoreThan1000():
    db.execute("SELECT itemcode, itemname, supplier FROM item2 WHERE cost>1000")
    items = db.fetchall()
    return None if len(items) == 0 else items


def getItemsSuppliedIn2020():
    db.execute("SELECT * FROM item2 WHERE date_supply LIKE '2020%'")
    items = db.fetchall()
    return None if len(items) == 0 else items


# main segment
res = initDatabase()
if res == None:
    exit()
db, sqlConn = initDatabase()

addInitialRecords()

while True:
    print(
        "1.Display the itemcode, itemname & supplier name, if the cost is more than 1000.\n2.Display the items supplied in the year 2020.\n3.Exit"
    )
    choice = int(input("Enter option (1-4) : "))

    if choice == 1:
        items = getItemsWithCostMoreThan1000()
        if items == None:
            print("No items with cost above 1000")
        else:
            print("Items with cost more than 1000 : ")
            for item in items:
                print(item)
    elif choice == 2:
        items = getItemsSuppliedIn2020()
        if items == None:
            print("No items supplied in 2020")
        else:
            print("Items supplied in 2020 : ")
            for item in items:
                print(item)
    elif choice == 3:
        break
    else:
        print("Invalid input")

    repeat = input("Repeat(Y/N)? : ")
    if repeat in "nN":
        break
closeDatabase()
