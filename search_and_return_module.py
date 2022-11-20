# import sqlite3
# Создание БД
# conn = sqlite3.connect('taxi_drivers.db')
# cur = conn.cursor()

# cur.execute("""CREATE TABLE drivers(
#    userid INT PRIMARY KEY,
#    full_name TEXT,
#    identification_number TEXT,
#    rating TEXT,
#    auto TEXT,
#    fines TEXT,
#    last_modified TEXT);
# """)
# conn.commit()


# drivers = [
#   ('1', 'Stephanie Stewart', '35659','4,8','Mazda','True', ''),
#   ('2', 'Sincere Sherman', '30819','3,9','Lada','False', ''),
#   ('3', 'Sidney Horn', '39798','4,5','Hyundai','False', ''),
#   ('4', 'Litzy Yates', '33899','4,4','Lada','False', ''),
#   ('5', 'Jaxon Mills', '31220','4,3','Ford','False', ''),
#   ('6', 'Paul Richard', '33565','4,7','Honda','True', ''),
#   ('7', 'Kamari Holden', '35612','4,2','Ford','True', ''),
#   ('8', 'Gaige Summers', '38515','4,9','Mazda','True', ''),
#   ('9', 'Andrea Snow', '37086','4,8','Kia','False', '')
# ]
#
# cur.executemany("INSERT INTO drivers VALUES(?, ?, ?, ?, ?, ?, ?);", drivers)
# conn.commit()

# cur.execute("SELECT * FROM drivers;")
# all_results = cur.fetchall()
# print(all_results)