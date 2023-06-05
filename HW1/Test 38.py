#Телефонный справочник


from functional import create
from interface import interface
path = "phone_book.txt"
create(path)
enter = 0
while enter != 4:
    enter = interface()
    if enter == 1:
        from functional import add_cont
        stroka = str(input("Введите ФИО и номер телефона "))
        add_cont(path, stroka)
    elif enter == 2:
        from functional import show_all
        print(show_all(path))
    elif enter == 3:
        from functional import search
        stroka = str(input("Введите фамилию "))
        search(path, stroka)
print("спасибо за работу")

def create(path):
    try:
        file = open(path, 'r')
    except IOError:
        print('Создан новый справочник -> phone_book.txt ')
        file = open(path, 'w')
    finally:
        file.close()

def add_cont(file_name, stroka):
    data = open(file_name, 'a')
    data.write(stroka + "\n")
    data.close()

def show_all(file_name):
    data = open(file_name, "r")
    for line in data:
        print(line[:-1])
    data.close()

def search(file_name, stroka):
    a = 0
    data = open(file_name, 'r')
    for line in data:
        if stroka in line:
            print(line)
            a = 123
            break
    if a != 123:
        print("нет такого")
    data.close()

def interface():
    print(" 1 - добавление контакта \n 2 - вывод всех \n 3 - поиск по фамилии \n 4 - выход")
    enter = int(input("Введите желаемый вариант "))
    return enter


from functional import *
from interface import start

path = "phone_book.txt"

start()

actions = {"1": "list",
           "2": "record",
           "3": "search",
           "4": "change",
           "5": "delete",
           "s": "stop"}
action = None

while action != "s":
    print("What can I do?", *[f"{i} - {actions[i]}" for i in actions])
    action = input()
    while action not in actions:
        print("What can I do?", *[f"{i} - {actions[i]}" for i in actions])
        action = input()
        if action not in actions:
            print("Data incorrect")
    if action != "s":
        if action == "1":
            print_records(path)
        elif action == "2":
            input_records(path)
        elif action == "3":
            find_records(path, *find_char())
        elif action == "4":
            change_records(path)
        elif action == "5":
            delete_records(path)


path = "phone_book.txt"
def print_records(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            print(*line.split(';'), end='')

def input_records(file_name: str):
    with open(file_name, 'r+', encoding='utf-8') as data:
        record_id = 0
        for line in data:
            if line != '':
                record_id = line.split(';', 1)[0]
        print('Enter FCS thru space')
        line = f'{int(record_id) + 1};' + ';'.join(input().split()[:4]) + ';\n'
        confirm = confirmation('add record')
        if confirm == 'y':
            data.write(line)

def find_char():
    print('Choose char: ')
    print('0 - id, 1 - second name, 2 - name, 3 - third name, 4 - number, s - stop')
    char = input()
    while char not in ('0', '1', '2', '3', '4', 's'):
        print('Data incorrect')
        print('Choose char: ')
        print('0 - id, 1 - second name, 2 - first name, 3 - third name, 4 - number, s - stop')
        char = input()
    if char != 's':
        inp = input('inter value\n')
        return char, inp
    else:
        return 's', 's'

def find_records(file_name: str, char, condition):
    if condition != 's':
        printed = False
        with open(file_name, 'r', encoding='utf-8') as data:
            for line in data:
                if condition == line.split(';')[int(char)]:
                    print(*line.split(';'))
                    printed = True
        if not printed:
            print("Nothing found")
        return printed

def check_id_record(file_name: str, text: str):
    decision = input(f'Do you know? {text}? 1 - yes, 2 - no, s -stop\n')
    while decision not in ('1', 's'):
        if decision != '2':
            print('Data incorrect')
        else:
            find_records(path, *find_char())
        decision = input(f'Do you know? {text}? 1 - yes, 2 - no, s -stop\n')
    if decision == '1':
        record_id = input('enter id, s - stop\n')
        while not find_records(file_name, '0', record_id) and record_id != 's':
            record_id = input('enter id, s - stop\n')
        return record_id
    return decision

def confirmation(text: str):
    confirm = input(f"Confirm {text} record: y - yes, n - no\n")
    while confirm not in ('y', 'n'):
        print('Data incorrect')
        confirm = input(f"Confirm {text} record: y - yes, n - no\n")
    return confirm

def replace_record_line(file_name: str, record_id, replaced_line: str):
    replaced = ''
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            replaced += line
            if record_id == line.split(';', 1)[0]:
                replaced = replaced.replace(line, replaced_line)
    with open(file_name, 'w', encoding='utf-8') as data:
        data.write(replaced)

def change_records(file_name: str):
    record_id = check_id_record(file_name, 'change')
    if record_id != 's':
        replaced_line = f'{int(record_id)};' + ';'.join(
            input('Enter\n').split()[:4]) + ';\n'
        confirm = confirmation('change')
        if confirm == 'y':
            replace_record_line(file_name, record_id, replaced_line)

def delete_records(file_name: str):
    record_id = check_id_record(file_name, 'delete')
    if record_id != 's':
        confirm = confirmation('change')
        if confirm == 'y':
            replace_record_line(file_name, record_id, '')

def start ():
    path = 'phone_book.txt'

    try:
        file = open(path, 'r')
    except IOError:
        print('New file created -> phone_book.txt ')
        file = open(path, 'w')
    finally:
        file.close()