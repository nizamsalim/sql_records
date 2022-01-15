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


def getItemsBySupplier(supplier):
    db.execute(f"SELECT * FROM item2 WHERE supplier='{supplier}'")
    items = db.fetchall()
    return None if len(items) == 0 else items


def increaseCostOfNestleProducts():
    db.execute("UPDATE item2 SET cost=1.1*cost WHERE supplier='nestle'")
    sqlConn.commit()
    return getItemsBySupplier('nestle')


# main segment
res = initDatabase()
if res == None:
    exit()
db, sqlConn = initDatabase()

addInitialRecords()

while True:
    print(
        "1.Display items of a supplier\n2.Increase the cost of all items supplied by Nestle, by 10%.\n3.Exit"
    )
    choice = int(input("Enter option (1-4) : "))

    if choice == 1:
        supplier = input("Enter supplier name : ")
        items = getItemsBySupplier(supplier)
        if items == None:
            print(f"No items supplied by {supplier}")
        else:
            print(f"Items supplied by {supplier} : ")
            for item in items:
                print(item)
    elif choice == 2:
        updatedNestleItems = increaseCostOfNestleProducts()
        print(f"Items supplied by Nestle(updated) : ")
        for item in updatedNestleItems:
            print(item)
    elif choice == 3:
        break
    else:
        print("Invalid input")

    repeat = input("Repeat(Y/N)? : ")
    if repeat in "nN":
        break
closeDatabase()
