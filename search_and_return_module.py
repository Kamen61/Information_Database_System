import sqlite3
conn = sqlite3.connect('taxi_drivers.db')
cur = conn.cursor()

# Создание БД
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
# cur.executemany("INSERT INTO drivers VALUES(?, ?, ?, ?, ?, ?, ?);", drivers)
# conn.commit()


# Вывод данных по параметрам
def search_param(list_param):
    # Создаем два списка . В списке list_keys находятся столбцы параметров поиска , в list_values находятся значения параметров поиска
    list_keys=[]
    list_values=[]
    all_columns = ["PRIMARY KEY", "full_name", "identification_number", "rating", "auto", "fines", "last_modified"]
    for i,j in enumerate(list_param):
        if j!='-1':
            list_keys.append(all_columns[i])
            list_values.append(j)
    sql_request = ''
    # Определяем сколько параметров передал пользователь и формируем запрос
    if len(list_keys) > 1:
        len_list=len(list_keys)
        count=0
        while len_list:
            sql_request+='{}="{}" AND '.format(list_keys[count],list_values[count])
            len_list-=1
            count+=1
        sql_request=sql_request[:-4]
        cur.execute(f"""SELECT * FROM drivers WHERE {sql_request}""")
    else:
        sql_request += '{}="{}"'.format(list_keys[0], list_values[0])
        cur.execute(f"""SELECT * FROM drivers WHERE {sql_request}""")
    return cur.fetchall()


# Вывод всех данных из таблицы
def search_all():
    cur.execute("SELECT * FROM drivers")
    return cur.fetchall()


print(search_all())