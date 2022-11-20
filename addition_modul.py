import sqlite3
import datetime

conn = sqlite3.connect('taxi_drivers.db')
cur = conn.cursor()
id_count = 10


def add_driver(data_list):
    global id_count
    full_name, license_number, rating, auto, fines = data_list
    last_modified = datetime.now()
    cur.execute("""INSERT INTO drivers(userid, full_name, identification_number, rating, auto, fines, last modified)
       VALUES(?, ?, ?, ?, ?, ?, ? );""", id_count, full_name, license_number, rating, auto, fines, last_modified)
    conn.commit()
    id_count += 1
