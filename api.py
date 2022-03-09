import mysql.connector
from fastapi import FastAPI

mydb = mysql.connector.connect(
    host="localhost:3306",
    user="root",
    passwd="itsamemariowahoo",
    database="robotics_parts_manifest"
)

cursor = mydb.cursor()
app = FastAPI()


@app.get("/")
async def root():
    return {"status": "OK"}


@app.post('/add/')
async def add(id, name, amount):
    exe = "INSERT INTO Parts (Id, PartName, Amount) VALUES (%s, %s, %s)"
    vals = (id, name, amount)

    cursor.execute(exe, vals)

    mydb.commit()

    return {cursor.rowcount, "record inserted."}


@app.post('/delete/')
async def delete(name):
    exe = "DELETE FROM Parts WHERE PartName = (%s)"
    vals = (name)

    cursor.execute(exe, vals)

    mydb.commit()

    return (cursor.rowcount, "record(s) deleted")


@app.get('/inventory/')
async def list():
    cursor.execute("SELECT * FROM Parts")

    result = cursor.fetchall()

    return (result)