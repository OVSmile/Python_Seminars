from add_contact_txt import add_new
from show_contact import show_all
from show_contact import show_name
from sorting import id_sort_list
from sorting import name_sort_list

def start():
      print('Меню контактов: '
          '\n\t1 - Добавить новый контакт.'
          '\n\t2 - Показать все контакты.'
          '\n\t3 - Показать только Имена и Фамилии контактов'
          '\n\t4 - Показать контакты упорядоченные по id'
          '\n\t5 - Показать контакты упорядоченные по Имени')

      choice = int(input('Введите номер желаемого действия: '))
      if choice == 1: print(add_new())
      elif choice == 2: print(show_all())
      elif choice == 3: print(show_name())
      elif choice == 4: print(id_sort_list())
      elif choice == 5: print(name_sort_list())











