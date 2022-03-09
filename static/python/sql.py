import mysql.connector
import argparse

argparser = argparse.ArgumentParser()

argparser.add_argument('-c', '--command')
argparser.add_argument('-id', '--id')
argparser.add_argument('-i', '--item')
argparser.add_argument('-a', '--amount')
argparser.add_argument('-l', '--list', action='store_true')

argvar = argparser.parse_args()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="robotics_parts_manifest"
)

cursor = mydb.cursor()


# CREATE TABLE Parts(Id int, PartName VARCHAR(255), Amount VARCHAR(255))

def add():
    id = argvar.id.lower()
    name = argvar.item.lower()
    amount = argvar.amount.lower()

    exe = "INSERT INTO Parts (Id, PartName, Amount) VALUES (%s, %s, %s)"
    vals = (id, name, amount)

    cursor.execute(exe, vals)

    mydb.commit()

    print(cursor.rowcount, "record inserted.")

    print(cursor.lastrowid)


def trolling():
    print('get trolled')


def delete():
    name = [argvar.item.lower()]

    exe = "DELETE FROM Parts WHERE PartName = (%s)"
    vals = name

    print(exe, vals)
    cursor.execute(exe, vals)

    mydb.commit()

    print(cursor.rowcount, "record(s) deleted")


def list():
    cursor.execute("SELECT * FROM Parts")

    result = cursor.fetchall()

    # loop through the rows
    for row in result:
        print(row)


def run():
    if argvar.command == 'a' or argvar.command == 'add':
        add()

    elif argvar.command == 'd' or argvar.command == 'delete':
        delete()

    if argvar.list:
        list()


if __name__ == "__main__":
    run()
