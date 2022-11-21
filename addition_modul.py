import sqlite3
import datetime

conn = sqlite3.connect('taxi_drivers.db')
cur = conn.cursor()
id_count = 10


def add_driver(data_list):
    global id_count
    data_list.insert(0,id_count)
    data_list.append(datetime.datetime.now())
    cur.execute("""INSERT INTO drivers VALUES(?, ?, ?, ?, ?, ?, ? );""", data_list)
    conn.commit()
    id_count += 1

# add_driver(['Perla Jefferson','30822','4,9','Mazda','False'])

