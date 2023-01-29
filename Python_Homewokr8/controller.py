import view
import model_student
import model_subject
import model_student_subject

def start():
    model_student.open_file()
    model_subject.open_file()
    model_student_subject.all_evaluations()

    choice = ''
    while choice != 11:
        choice = view.main_menu()
        match choice:
            case 1: #'Cохранить изменения'
                model_student.save_file_stud()
                model_subject.save_file_subj()

            case 2: #'Список студентов'
                view.show_students(model_student.get_data_student())
            case 3: #Добавить студента в список'
                new_student = view.new_student()
                model_student.add_new_student(new_student)
            case 4: #'Удалить студента из списка'
                del_stud = view.delete_student()
                model_student.delete_student(del_stud)
                model_student_subject.all_evaluations()
            case 5: #'Добавить предмет'
                view.show_subject(model_subject.get_data_subject())
            case 6: #'Удалить предмет из списка'
                new_subject = view.new_subject()
                model_subject.add_new_subject(new_subject)
            case 7: #'Добавить оценку ученику'
                name, subj, grad = view.input_grades()
                model_student_subject.add_grades(name, subj, grad)
            case 8: #'Оценки учеников по предметам'
                find = view.find_student()
                if find == '1':
                    students_subject = model_student_subject.all_evaluations()
                    view.show_students_subject(students_subject)
                else:
                    search = model_student_subject.student_evaluations(find)
                    view.show_students_subject(search)
            case 9: #'Средняя успеваемость студентов'
                list = model_student_subject.all_evaluations()
                view.show_midle_evaluations(list)
            case 10:
                pass
            case _:
                view.input_error()

