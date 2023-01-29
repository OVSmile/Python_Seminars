import view
import model_example


def start():

    exam = view.get_example()
    res = model_example.get_result(exam)
    view.show_result(exam, res)


