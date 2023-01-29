import model_student
import model_subject


student_subject = {}

def get_student_subject():
    global student_subject
    return student_subject

def all_evaluations():
    global student_subject
    student_subject = {}
    student_list = model_student.get_data_student()
    subjekt_dict = model_subject.get_data_subject()
    for i in range(len(student_list)):
        name_soname = student_list[i]
        student_subject[name_soname] = subjekt_dict
    print(student_list)
    print(student_subject)
    return student_subject


def student_evaluations(search):
    global student_subject
    search_list = {}
    for name, info in student_subject.items():
        if search in name:
            search_list[name] = info
    return search_list

def add_grades(name, subj, grad):
    global student_subject
    for student in student_subject.keys():
        if name in student:
            student_subject[student][subj].append(int(grad))






