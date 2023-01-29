
def get_example():
    example = input('Введите арифметическое выражение: ')
    return example

def show_result(exam, res):
    print(f'{exam} = ', end='')
    print(*res)

