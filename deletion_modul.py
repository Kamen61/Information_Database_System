import sqlite3

conn = sqlite3.connect('taxi_drivers.db')
cur = conn.cursor()


def add_driver(user_id):
    cur.execute("""DELETE FROM drivers WHERE userid=?;""", user_id)
    conn.commit()

# def add_driver(user_id):
#     cur.execute(f"""DELETE FROM drivers WHERE userid={user_id};""")
#     conn.commit()
#
# add_driver('10')