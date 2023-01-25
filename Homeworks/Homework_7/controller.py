
import view
import model


def start():
    option = view.menu()  # отображение меню
    if option == 1:
        print('Введите имя текстового файла (tel_db.txt) для добавления информации')
        file_name = view.get_file_name_to_read()  # ввод имени текстового файла
        a=''
        while a!= 'exit':
            # подсчет количества строк в файле
            count = model.count_lines(file_name)
            # добавление записи (новой строки) в текстовый файл
            model.add_person(file_name, count)
            a=input(f"{'='*20}\nВыйти ?\nда=ввести exit, нет=нажать enter: ")
    elif option == 2:
        print('Введите имя текстового файла (tel_db.txt) для экспорта в *.json')
        file_name_1 = view.get_file_name_to_read()  # ввод имени текстового файла
        # преобразование инфо из текстового файла в словарь
        dict = model.convert_txt_to_dictionary(file_name_1)
        print('Введите имя json файла (tel_db.json) для сохранения на диск')
        file_name_2 = view.get_file_name_to_write()  # ввод имени json файла
        model.write_json(file_name_2, dict)  # запись json файла
    elif option == 3:
        print('Введите имя текстового файла (tel_db.txt) для экспорта в *.csv')
        file_name_3 = view.get_file_name_to_read()  # ввод имени текстового файла
        # преобразование инфо из текстового файла в список
        list = model.convert_txt_to_list(file_name_3)
        print('Введите имя csv файла (tel_db.csv) для сохранения на диск')
        file_name_4 = view.get_file_name_to_write()  # ввод имени csv файла
        model.write_csv(file_name_4, list)  # запись csv файла
    elif option == 4:
        print('Введите имя json файла (tel_db.json) для импорта в *.txt')
        file_name_5 = view.get_file_name_to_read()  # ввод имени json файла
        data = model.import_json_as_txt(file_name_5)  # чтение файла json
        print('Введите имя txt файла (tel_db_1.txt) для сохранения на диск')
        file_name_6 = view.get_file_name_to_write()  # ввод имени txt файла
        model.save_as_txt_from_json(file_name_6, data)  # запись txt файла
    elif option == 5:
        print('Введите имя csv файла (tel_db.csv) для импорта в *.txt')
        file_name_7 = view.get_file_name_to_read()  # ввод имени csv файла
        rows = model.import_csv_as_txt(file_name_7)  # чтение файла csv
        print('Введите имя txt файла (tel_db_2.txt) для сохранения на диск')
        file_name_8 = view.get_file_name_to_write()  # ввод имени txt файла
        model.save_as_txt_from_csv(file_name_8, rows)  # запись txt файла
    return
