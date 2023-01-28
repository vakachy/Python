
import csv
import json
import view


def Get_employees():
    with open('db.txt', 'r', encoding='utf-8') as txtfile:
        content = txtfile.read().split('\n')
    employees = []
    for row in content:
        items = row.strip().split(';')
        temp = {}
        temp["id"] = items[0].strip()
        temp["full_name"] = items[1].strip()
        temp["phone_number"] = items[2].strip()
        temp["occupation"] = items[3].strip()
        temp["salary"] = items[4].strip()
        employees.append(temp)
    return employees
# -------------------------------------------------------------------- #


def Find_employee(employyes, employee):
    result=[]
    for item in employyes:
        for v in item.values():
            if employee in v:
                result.append(item)
    return result
# -------------------------------------------------------------------- #


def Pick_employee(employees, criterion):
    result = []
    for item in employees:
        if item['occupation'] == criterion:
            result.append(item)
    return result
# -------------------------------------------------------------------- #

def Select_employee(employees, criterion):
    result_less_than = []
    result_more_than = []
    for item in employees:
        # for v in item['salary']:
            if float(criterion) <= float(item['salary']):
                result_less_than.append(item)
            else:
                result_more_than.append(item)
    return result_less_than, result_more_than

# -------------------------------------------------------------------- #



def Add_employee(employee):
    line =';'.join([str(v) for v in employee.values()])
    with open ('db.txt', 'a', encoding='utf-8') as txtfile:
        txtfile.write('\n'+line)
# -------------------------------------------------------------------- #


def Remove_employee(employees):
    id = view.Get_id_for_deletion()
    for item in employees:
        if item['id'] == id:
            item.clear()

    content=[]
    with open ('db.txt', 'w', encoding='utf-8') as txtfile:
        for line in employees:
            if line:
                line =';'.join([str(v) for v in line.values()])
                content.append(line)
        txtfile.write('\n'.join(content))
# -------------------------------------------------------------------- #


def Update_employee(employees):
    id, field, data = view.Enter_employee_new_data()
    for item in employees:
        if item['id'] == id:
            item[field] = data

    content=[]
    with open ('db.txt', 'w', encoding='utf-8') as txtfile:
        for line in employees:
            if line:
                line =';'.join([str(v) for v in line.values()])
                content.append(line)
        txtfile.write('\n'.join(content))
# -------------------------------------------------------------------- #
# save as json


def write_json(list,file_name):
    with open(file_name, "w", encoding='utf-8') as out_file:
        json.dump(list, out_file, indent = 4)
# -------------------------------------------------------------------- #
# save as csv


def write_csv(list, file_name):

    fields = ['id', 'full_name', 'phone_number', 'occupation','salary']
    with open(file_name, "w", encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields, lineterminator='\n')
        writer.writeheader()
        writer.writerows(list)
