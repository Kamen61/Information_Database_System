import PySimpleGUI as sg
import deletion_modul
# from change_module import sql_update

def get_change_info(id_num):
    window_change_layout = [
        [sg.Text('Заполните строки для внесения изменений в запись')],
        [sg.Text('Полное имя:'), sg.Input(key='full_name')],
        [sg.Text('Водительское удостоверение:'), sg.Input(key='identification_number')],
        [sg.Text('Рейтинг:'), sg.Input(key='rating')],
        [sg.Text('Автомобиль')],
        [sg.Combo(values=['Mazda', 'Lada', 'Hyundai', 'Ford', 'Honda', 'Kia'], size=(45, 10), key='auto')],
        [sg.Text('Наличие непогашенных штрафов')],
        [sg.Combo(values=['True', 'False'], size=(20, 10), key='fines')],
        [sg.Button('Внести изменения'), sg.Button('Отмена')]
    ]

    window_change = sg.Window('Изменение данных водителя', window_change_layout, modal=True, finalize=True)

    while True:        
        event, value = window_change.read()
        if event in (sg.WIN_CLOSED, 'Отмена'):
            break
            # window_change.close()
        if event == 'Внести изменения':
            info_for_change = []
            info_for_change = [id_num, value['full_name'], value['identification_number'], value['rating'], value['auto'], value['fines']]
            print(info_for_change)
            window_change.close()
            return info_for_change
            # break
    # window_change.close()


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
        [sg.Button('Изменить'), sg.Button('Удалить'), sg.Button('Вернуться')],
    ]

    table_window = sg.Window('Режим просмотра водителей', table_layout, modal=True)

    while True:
        event, value = table_window.read()

        if event == 'SQL_TABLE':
            request = sql_request_search[value['SQL_TABLE'][0]]
            id_driver = request[0]
            print(request)
            print(id_driver)
            print(type(id_driver))

        
        if event in (sg.WIN_CLOSED, 'Вернуться'):
            break
            
            
        if event == 'Удалить':  
            if value['SQL_TABLE']==[]:
                sg.popup('Нет данных для удаления') 
            else:
                deletion_modul.add_driver(id_driver)
                table_window.close()
                sg.popup('Запись удалена') 

                # table_window[request].update([]) 

        if event == 'Изменить':
            if value['SQL_TABLE']==[]:
                sg.popup('Нет данных для изменения') 
            else:
                info_change = get_change_info(id_driver)
                print(info_change)      
            # sql_update(info_change)
            # вызов команды sql изменить (info_change)
        


    table_window.close()

# show_table(sql_request_search, headings)

# show_table(sql_request_search, headings)
