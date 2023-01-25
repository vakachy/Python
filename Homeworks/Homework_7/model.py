import json
import csv
import view

# ----------------------------------------------------------------------- #
# для работы с чтением текстового файла, преобразованием инфо
# в словарь и последующей записи *.json


# convert txt to dict
def convert_txt_to_dictionary(file_name):
    dict={}
    with open(file_name,'r', encoding='utf-8') as f:
        for line in f:
            id,tel,full_name,place = line.strip().split(';')
            dict[id]=[tel,full_name,place]
    return dict


# save as json
def write_json(file_name, dict):
    with open(file_name, "w", encoding='utf-8') as out_file:
        json.dump(dict, out_file, indent = 4)
# ----------------------------------------------------------------------- #
# для работы с добавлением записей в текстовый файл


def add_person(file_name, count):
    with open (file_name,'a', encoding='utf-8') as f:
        tel, full_name, place = view.add_person()
        f.write('\n' + f"id_{count+1};{tel};{full_name};{place}")


# count lines in a *.txt file
def count_lines(file_name):
    count = 0
    with open (file_name,'r', encoding='utf-8') as f:
        content = f.readlines()
        count=len(content)
        # for line in content:
        #     count+=1
    return count
# ----------------------------------------------------------------------- #
# для работы с текстовым файлом:
# преобразование строк в список списков
# запись *.csv


# convert txt to list of lists
def convert_txt_to_list(file_name):
    l_total=[]
    with open(file_name,'r', encoding='utf-8') as f:
        for line in f:
            l = line.strip().split(';')
            l_total.append(l)
    return l_total


# save as csv
def write_csv(file_name, l_total):
    with open(file_name, "w", encoding='utf-8') as out_file:
        # fields = ['id','Телефон','Фамилия И. О.','Город']
        writer = csv.writer(out_file, delimiter=';', lineterminator='\n')
        # writer.writerow(fields)
        writer.writerows(l_total)
# ----------------------------------------------------------------------- #
# для работы с *.csv:
# чтение из файла *.csv
# преобразование строк файла в тип string
# запись *.txt


# read a csv file
def import_csv_as_txt(file_name):
    # fields = []
    rows = ''
    with open(file_name,'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for line in csvreader:
            if line:
                row_str=' '.join(i for i in line)
                rows+=row_str + '\n'
        return rows


# write/save a txt file
def save_as_txt_from_csv(file_name, rows):
    with open(file_name, 'w', encoding='utf-8') as txtfile:
        txtfile.write(rows)
# ----------------------------------------------------------------------- #
# для работы с *.json:
# чтение из файла *.json
# преобразование строк файла в тип string (в файле *.json данные в виде словаря)
# запись *.txt


# read a json file
def import_json_as_txt(file_name):
    str=''
    with open(file_name,'r',encoding='utf-8') as file:
        data = json.load(file)
        s=''
        for k,v in data.items():
            str=''
            str+=k+';' + ';'.join(i for i in v)
            s+=str+'\n'
        # print(s)
    return s


# write/save a file
def save_as_txt_from_json(file_name, data):
    with open(file_name,'w',encoding='utf-8') as file:
        file.write(data)
# ----------------------------------------------------------------------- #