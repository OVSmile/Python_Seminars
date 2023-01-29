data_students = []
path = 'data_student.txt'

def open_file():
    global data_students
    global path
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for one_student in file:
        data_students.append(one_student.strip())
    print(data_students)

def save_file_stud():
    global data_students
    global path
    subj_list = []
    for subj in data_students:
        subj_list.append(subj)
    print(subj_list)
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(subj_list))

def get_data_student():
    global data_students
    return data_students

def add_new_student(new_student):
    global data_students
    data_students.append(new_student)

def delete_student(name):
    global data_students
    data_students.remove(name)
    print(type(data_students))


