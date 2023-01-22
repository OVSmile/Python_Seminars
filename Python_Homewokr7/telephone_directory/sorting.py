from show_contact import contacts_list

def id_sort_list():
    contacts = sorted(contacts_list(), key=lambda x: int(x[0]))
    for i in contacts:
        print(f'Контакт №{i[0]}'
              f'\n\tИмя: {i[1]}'
              f'\n\tФамилия: {i[2]}'
              f'\n\tНомер телефона: {i[3]}'
              f'\n\tКоментарий: {i[4]}')

def name_sort_list():
    contacts = sorted(contacts_list(), key=lambda x: x[1])
    for i in contacts:
        print(f'Контакт №{i[0]}'
              f'\n\tИмя: {i[1]}'
              f'\n\tФамилия: {i[2]}'
              f'\n\tНомер телефона: {i[3]}'
              f'\n\tКоментарий: {i[4]}')
