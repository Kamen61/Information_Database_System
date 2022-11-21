import sqlite3
import main
import datetime


conn = sqlite3.connect('taxi_drivers.db')
cur = conn.cursor()
list_param = main.FV                         # входящий список изменяющихся значений ,берет из модуля main
all_columns = ["PRIMARY KEY", "full_name", "identification_number", "rating", "auto", "fines", "last_modified"]

def sql_update(conn, list_param, all_columns):    # принимает connect, входящий спискок изменений и названия всех полей
    now = datetime.datetime.now()
    time = now.strftime("%d-%m-%Y %H:%M")

    for i in range(1, len(list_param)):
        if not list_param[i]:
            print('Not value')
        else:                      # изменяет данные в соответствуещем поле
            cur.execute(f' UPDATE drivers SET {all_columns[i]} = "{list_param[i]}" where userid = {list_param[0]}')

    cur.execute(f' UPDATE drivers SET {all_columns[6]} = "{time}" where userid = {list_param[0]}')  # вносит дату и время

    return cur.execute(f'SELECT * FROM drivers where userid = {list_param[0]} ')     # возвращает обновленные данные


sql_update(conn, list_param, all_columns)   #  вызов функции изменений

print(cur.fetchall())
