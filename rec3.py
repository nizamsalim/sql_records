import mysql.connector as ms


def initDatabase():
    sqlConn = ms.connect(host="localhost", user="root", password="nizam123")

    if sqlConn.is_connected() == False:
        print("Connection failed")
        return None
    else:
        db = sqlConn.cursor()
        db.execute("CREATE DATABASE IF NOT EXISTS student")
        db.execute("USE student")
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS marks(
                stcode INT(3),
                stname VARCHAR(25),
                term1 INT(3),
                term2 INT(3),
                total INT(3)
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
    n = int(input("Number of records to add : "))
    k = 0
    for i in range(n):
        stCode = int(input("Student code : "))
        stName = input("Student name : ")
        tm1 = int(input("Term 1 marks : "))
        tm2 = int(input("Term 2 marks : "))
        tot = tm1 + tm2
        db.execute(
            f"INSERT INTO marks VALUES({stCode},'{stName}',{tm1},{tm2},{tot})")
        k = 1
    if k == 1:
        sqlConn.commit()


def getNamesWithHighestTotal():
    db.execute(
        """
        SELECT stname FROM marks WHERE total=(SELECT MAX(total) from marks)
        """
    )
    return db.fetchall()


def sortByTotalMarks():
    db.execute(
        """
        SELECT * FROM marks ORDER BY total
        """
    )
    return db.fetchall()


def getNamesWithTotalLessThan100():
    db.execute(
        """
        SELECT * FROM marks WHERE total<100
        """
    )
    return db.fetchall()


# main segment
res = initDatabase()
if res == None:
    exit()
db, sqlConn = res

addInitialRecords()

while True:
    print(
        "1.Highest total\n2.Sort according to total marks\n3.Total marks less than 100\n4.exit"
    )
    choice = int(input("Enter option (1-4) : "))

    if choice == 1:
        toppers = getNamesWithHighestTotal()
        print("Toppers : ")

        for topper in toppers:
            print(topper[0])

    elif choice == 2:
        sortedRecords = sortByTotalMarks()
        print("Sorted records : ")

        for student in sortedRecords:
            print(student)

    elif choice == 3:
        students = getNamesWithTotalLessThan100()
        print("Students with total less than 100 : ")

        for student in students:
            print(student)
    elif choice == 4:
        break
    else:
        print("Invalid input")

    repeat = input("Repeat(Y/N)? : ")
    if repeat in "nN":
        break
closeDatabase()
