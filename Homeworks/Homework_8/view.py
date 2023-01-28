
import model

def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

# -------------------------------------------------------------------- #
# ввод параметра для поиска сотрудника: имя, фамилия, номер телефона, город...

def Look_for_employee():
    print('='*20)
    print("Поиск сотрудника")
    print('='*20)
    employee = input("Введите имя сотрудника: ")
    return employee
# -------------------------------------------------------------------- #
# вывод инфо о найденных сотрудниках в консоль

def Show_employee(result):
        print("-"*20)
        print("Найдено в БД")
        print("-"*20)
        for item in result:
            for k,v in item.items():
                print(f'{k}: {v}')
            print('*'*20)
        return
# -------------------------------------------------------------------- #


def Show_employee_selection(selection_1, selection_2):
        print("-"*20)
        print("Найдено в БД")
        print("-"*20)
        print("+"*50)
        print("Найдено с зарплатой больше/равно заданной: ")
        print("+"*50)
        for item in selection_1:
            for k,v in item.items():
                print(f'{k}: {v}')
            print('*'*20)
        print("+"*50)
        print("Найдено с зарплатой меньше заданной: ")
        print("+"*50)
        for item in selection_2:
            for k,v in item.items():
                print(f'{k}: {v}')
            print('*'*20)
        return
# -------------------------------------------------------------------- #
# ввод параметра для выборки сотрудников из БД

def Get_selection_criterion_for_occupation():
    print('='*20)
    print("Выборка сотрудников по должности: ")
    print('='*20)
    criterion = input("Введите должность для выборки сотрудников: ")
    return criterion
# -------------------------------------------------------------------- #
# ввод параметра для выборки сотрудников из БД

def Get_selection_criterion_for_salary():
    print('='*20)
    print("Выборка сотрудников по зарплате: ")
    print('='*20)
    criterion = input("Введите зарплату для выборки сотрудников: ")
    return criterion
# -------------------------------------------------------------------- #


def Addition_of_employee():
    count = len(model.Get_employees())
    i=0
    employee = {}
    fields = ['full_name', 'phone_number', 'occupation', 'salary']
    message = ['Полное имя','Номер телефона','Профессия','Зарплата']
    employee['id']=count+1
    print('='*20)
    print("Добавление сотрудника")
    print('='*20)
    for item in fields:
        employee[item] = input(f'Введите данные в поле "{message[i]}": ')
        i+=1
    return employee
# print(Addition_of_employee())
# -------------------------------------------------------------------- #


def Get_id_for_deletion():
    print('='*20)
    print("Удаление сотрудника из БД")
    print('='*20)
    id = input("Введите ID сотрудника: ")
    return id
# -------------------------------------------------------------------- #


def Enter_employee_new_data():
    print('='*20)
    print("Обновить данные сотрудника в БД")
    print('='*20)
    id = input("Введите ID сотрудника: ")
    field = input("Введите поле для изменения данных:\n(\"full_name/phone_number/occupation/salary\"): ")
    data = input("Введите новое значение: ")
    
    return id, field, data
# -------------------------------------------------------------------- #