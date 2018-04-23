import sqlite3

db_conn = sqlite3.connect('dice_stats.db')


def initialize():
    db_conn.execute("DROP TABLE IF EXISTS dice_stats")
    db_conn.commit()
    try:
        db_conn.execute(
            "CREATE TABLE dice_stats(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Num INTEGER NOT NULL);")
        db_conn.commit()

        print("Table Created")

    except sqlite3.OperationalError:
        print("Table couldn't be Created")


def insert_in_db(x):
    db_conn.execute("INSERT INTO dice_stats(Num) VALUES ('" + str(x) + "')")


def get_all6_stats():
    cursor = db_conn.cursor()
    try:
        result = cursor.execute("SELECT Num FROM dice_stats")
        for item in result:
            yield item

    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")

    except:
        print("Couldn't Retrieve Data From Database")


initialize()
