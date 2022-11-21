import PySimpleGUI as sg

def show_table(sql_request_search, headings):
    table_layout = [
        [sg.Table(sql_request_search, headings=headings,
        max_col_width=50,
        auto_size_columns=True,
        display_row_numbers=True, # отображает row в таблице
        justification='center',
        num_rows=20,
        enable_events=True, # можно выбирать строки сразу в таблице и совершать действия 
        key='SQL_TABLE',
        row_height=25)],
        [sg.Button('Изменить', key='CHANGE_BUTTON'), sg.Button('Удалить', key='DELITE_BUTTON')],
    ]

    table_window = sg.Window('Режим просмотра водителей', table_layout)
    while True:
        event, value = table_window.read()
        if event in (sg.WIN_CLOSED, 'Выход'):
            break
        if event == 'SQL_TABLE':
            print(value['SQL_TABLE'][0])
            sql_request = sql_request_search[value['SQL_TABLE'][0]]
            print(sql_request)
            
        # if event == 'Изменить':
            # вызов команды sql изменить (sql_request)
        
        # if event == 'Удалить':
            # вызов команды sql изменить (sql_request)
            

    table_window.close()

# show_table(sql_request_search, headings)
