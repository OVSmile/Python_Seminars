def new_contact():
    new_cont = ''
    print('Заполните данные нового контакта')
    new_cont += f"{input('Введите id: ')} " \
                f"{input('Введите Имя: ')} " \
                f"{input('Введите Фамилия: ')} " \
                f"{input('Введите номер телефона: ')} " \
                f"{input('Введите коментарий к контакту: ')}"
    return new_cont

