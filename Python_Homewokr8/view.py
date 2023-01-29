comands = ['Cохранить изменения',
           'Список студентов',
           'Добавить студента в список',
           'Удалить студента из списка',
           'Cписок предметов',
           'Добавить предмет',
           'Добавить оценку ученику',
           'Оценки учеников по предметам',
           'Средняя успеваемость студентов',
           'Студенты претендующие на золотую медаль',
           'Закончить работу',
           ]

def main_menu() -> int:
    print('Главное меню:')
    for i, item in enumerate(comands, 1):
        print(f'\t{i}. {item}')
    choice = int(input('Выберете пункт меню: '))
    return choice

def show_students(student_list):
    if len(student_list) < 1:
        print('Файл список студентов пуст')
    else:
        for i, student in enumerate(student_list, 1):
            print(f'\t{i}. {student:20}')

def show_subject(subject_list):
    if len(subject_list) < 1:
        print('Файл список предметов пуст')
    else:
        for i, subject in enumerate(subject_list, 1):
            print(f'\t{i}. {subject:10}')

def show_students_subject(students_subject_list):
   if len(students_subject_list) < 1:
        print('Файл/список пуст')
   else:
        for name, info in students_subject_list.items():
            print(f'{name}: ')
            for subj, list_grades in info.items():
                print(f'\t{subj} {list_grades}')

def show_midle_evaluations(students_subject_list):
    print('Средний балл по предметам: \n')
    for info in students_subject_list.values():
        subj_grades = []
        for sabj, grades in info.items():
            subj_grades += grades
            if len(subj_grades) > 0:
                print(f'\t{info} {sum(subj_grades) / len(subj_grades)}')
            else:
                print(f'\t{info} 0')

def input_error():
    print('Ошибка ввода')

def new_student():
    name = input('Введите имя ученика: ')
    soname = input('Введите фамилию ученика: ')
    name_soname = name + ' ' + soname
    print('Данные студента добавлены в список\n')
    return name_soname

def delete_student():
    name = input('Введите имя ученика: ')
    return name

def new_subject():
    item_name = input('Введите название предмета: ')
    print('Новый предмет добавлен в список.\n')
    return item_name

def find_student():
    print('1. Список всех учеников\n'
          '2. Поиск по имени ученика')
    find = input('Выберете действие: ')
    if find == '1': return find
    elif find == '2':
        find = input('Введите имя ученика: ')
        return find
    else:
        input_error()

def input_grades():
    name = input('Введите имя ученика: ')
    subj = input('Введите название предмета: ')
    grad = input('Введите оценку: ')
    print(f'Оценка добавлена в список оценок ученика.')
    return name, subj, grad




