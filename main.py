import PySimpleGUI as sg
import view_table
from datetime import date
import search_and_return_module as search
import addition_modul


layout = [
    [sg.Text('Главное меню программы')],
    [sg.Text('Заполните необходимы строки и выберите дальнейшее действие')],
    [sg.Text('ID Сотрудника:'), sg.Input(key='userid')],
    [sg.Text('Полное имя:'), sg.Input(key='full_name')],
    ## Проверить на заполнение: [sg.Text('Полное имя:'), sg.Input(key='full_name', do_not_clear=False, size=МОЖНО ЗАДАТЬ РАЗМЕР)],
    [sg.Text('Водительское удостоверение:'), sg.Input(key='identification_number')],
    [sg.Text('Рейтинг:'), sg.Input(key='rating')],
    [sg.Text('Выберите автомобиль из автопарка на котором работает водитель')],
    [sg.Combo(values=['Mazda', 'Lada', 'Hyundai', 'Ford', 'Honda', 'Kia'], size=(45, 10), key='auto')],
    [sg.Text('У водителя есть непогашенные штрафы?')],
    [sg.Combo(values=['True', 'False'], size=(20, 10), key='fines')],
    # [sg.Radio('Нет', 'RADIO', key='finesNo'), sg.Radio('Да', 'RADIO', key='finesYes')],  # второй вариант оформления опции наличия штрафов
    [sg.Text('Для изменения или удаления водителя из базы данных найдите его через поиск')],
    [sg.Button('Поиск'), sg.Button('Добавить'), sg.Button('Выход')]
    # [sg.Button('Поиск'), sg.Button('Добавить'), sg.Button('Изменить'), sg.Button('Удалить'), sg.Button('Выход')] # вариант где опции изменить и удалить в общем меню
]

sg.theme('LightBlue2')
window = sg.Window('Список водителей', layout)

while True:
    event, value = window.read()
    if event in (sg.WIN_CLOSED, 'Выход'):
        break
    elif event == 'Поиск':
        headings = ['userid', 'full_name', 'identification_number', 'rating', 'auto', 'fines', 'last_modified']
        sql_request_search = []
        # last_modified = datetime.datetime.now()
        sql_request_search = [value['userid'], value['full_name'], value['identification_number'], value['rating'], value['auto'], value['fines']]
        # print(sql_request_search) # тест(вывод значения в консоль)
        ## функция передачи переменной в запрос sql
        # Возврат переменной из sql

        # Добавил немного логики. Если пользователь ничего не ввел в строках то ему выдается вся бд. Если ввел то выводится подходящие данные
        count=0
        for i in sql_request_search:
            if i!='':
                count+=1
        if not count:
            sql_request_search = search.search_all()
            view_table.show_table(sql_request_search, headings)
        else:
            result=search.search_param(sql_request_search)
            view_table.show_table(result,headings)  # для теста в переменную вставлена инфо из ввода, должна прийти из запроса sql (sql_request_search изменить на переменную от sql)
        # sg.popup(f'Создана новая запись {sql_request_search}')

    elif event == 'Добавить':
       sql_request_add = []
       sql_request_add = [value['full_name'], value['identification_number'], value['rating'], value['auto'], value['fines']]
       # Проверка на пустые строки!
       addition_modul.add_driver(sql_request_add)
       sg.popup(f'Добавлена новая запись: {sql_request_add}')
        
        
#     elif event == 'Изменить': # Функция перенесена  в блок поиска
#     elif event == 'Удалить': # Функция перенесена  в блок поиска
        
        
        
        









##=================================================================================================
# # This is a sample Python script.

# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
