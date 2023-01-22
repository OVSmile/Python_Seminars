from create_pathname import path_name

def contacts_list():
    path = path_name()
    contacts = []
    data = open(path, 'r')
    for line in data:
        contacts.append(list(line.split(' ')))
    data.close()
    return contacts
print(contacts_list())

def show_all():
    list_all = contacts_list()
    for i in list_all:
        print(f'Контакт №{i[0]}'
              f'\n\tИмя: {i[1]}'
              f'\n\tФамилия: {i[2]}'
              f'\n\tНомер телефона: {i[3]}'
              f'\n\tКоментарий: {i[4]}')

def show_name():
    list_all = contacts_list()
    for i in list_all:
        print(f'Имя: {i[1]}'
              f'\nФамилия: {i[2]}\n')



