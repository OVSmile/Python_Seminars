

data_subjects = {}
path = 'data_grades.txt'

def open_file():
    global data_subjects
    global path
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for one_subj in file:
        data_subjects[one_subj.strip()] = []

def save_file_subj():
    global data_subjects
    global path
    subj_list = []
    for subj in data_subjects.keys():
        subj_list.append(subj)
    print(subj_list)
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(subj_list))

def get_data_subject():
    global data_subjects
    return data_subjects

def add_new_subject(new_subject):
    global data_subjects
    data_subjects[new_subject] = []
