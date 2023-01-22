from entering_contact import new_contact
from create_pathname import path_name

def add_new():
    path = path_name()
    data = open(path, 'a')
    data.write(f'{new_contact()}\n')
    data.close()
