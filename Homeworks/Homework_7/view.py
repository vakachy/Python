
def menu():
    print('Выбрать необходимое действие:')
    print('1 - "добавить запись в справочник"')
    print('2 - "экспорт *.txt --> *.json"')
    print('3 - "экспорт *.txt --> *.csv"')
    print('4 - "импорт *.txt <-- *.json"')
    print('5 - "импорт *.txt <-- *.csv"')

    option = int(input('Ввести номер операции: '))
    return option


def add_person():
    print('Введите данные в справочник')
    tel = input('Телефон: ')
    full_name = input('Фамилия И. О.: ')
    place = input('Город: ')
    return tel, full_name, place


# enter file name to read
def get_file_name_to_read():
    file_name = input('Введите имя файла для чтения: ')
    return file_name


# enter file name to write
def get_file_name_to_write():
    file_name = input('Введите имя файла для записи: ')
    return file_name
