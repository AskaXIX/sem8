# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
# 1. Программа должна выводить данные 
# 2. Программа должна сохранять данные в текстовом файле 
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека) 
# 4. Использование функций. Ваша программа не должна быть линейной


def initial_note():
    with open('phone.txt', 'a', encoding='UTF-8') as data:
        data.write('Ивано Иван Васильевич 11111\n')

def add_contact():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    lastname = input('Введите отчество: ')
    phone_num = input('Введите номер: ')
    while not phone_num.isdigit():
        phone_num = input('Введите номер: ')
    str = f'{surname} {name} {lastname} {phone_num}\n'
    with open('phone.txt', 'a', encoding='UTF-8') as data:
        data.write(str)

def search_contact(str):
    with open('phone.txt', 'r', encoding = 'UTF-8') as data:
        for line in data:
            if str.lower() in line.lower().split():
                print(line, end = '')

def delete_contact(str):
    lst = []
    with open('phone.txt', 'r', encoding='UTF-8') as data:
        lst = data.readlines()
        for line in range(len(lst)):
            if str.lower() in lst[line].lower().split():
                lst[line] = ''
    with open('phone.txt', 'w', encoding='UTF-8') as data:
        for i in lst:
            data.write(i)

def edit_contact(str):
    delete_contact(str)
    add_contact()

while True:
    text = input('\n Добро пожаловать в телефонный справочник! \n\n Вывести список - all \n Добавить контакт - add \n Найти контакт - find \n Изменить контакт - ed \n Удалить контакт - del \n Выйти - stop \n\n Пожалуйста выберите, что нужно сделать?: ')
    if text.lower() == 'stop':
        break
    if text.lower() == 'add':
        add_contact()
    if text.lower() == 'find':
        str = input('Что ищете? ')
        search_contact(str)
    if text.lower() == 'all':
        search_contact('')
    if text.lower() == 'del':
        str = input('Что ищете? ')
        delete_contact(str)
    if text.lower() == 'ed':
        str = input('Что ищете? ')
        edit_contact(str)