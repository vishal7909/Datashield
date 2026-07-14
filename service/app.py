from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pymysql

app = FastAPI()

DB_HOST = "DB-HOST-URL"
DB_USER = "admin"
DB_PASSWORD = "PASSWORD"
DB_NAME = "DBNAME"


@app.get("/", response_class=HTMLResponse)
def dashboard():
    with open("templates-static/index.html") as f:
        return f.read()


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/metadata")
def receive_metadata(payload: dict):

    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    cursor = connection.cursor()

    filename = payload.get("file", "unknown")
    filesize = payload.get("size", 0)

    cursor.execute(
        """
        INSERT INTO metadata(filename, filesize)
        VALUES(%s, %s)
        """,
        (filename, str(filesize))
    )

    connection.commit()

    cursor.close()
    connection.close()

    return {
        "status": "stored",
        "filename": filename,
        "filesize": filesize
    }


@app.get("/files")
def get_files():

    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM metadata")

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return {
        "records": rows
    }