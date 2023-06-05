#Задача 38: Дополнить телефонный справочник возможностью изменения и 
#удаления данных. Пользователь также может ввести фамилию, и Вы должны 
#реализовать функционал для изменения и удаления данных


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