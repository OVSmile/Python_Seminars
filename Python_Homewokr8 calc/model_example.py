
def get_result(example):
    example = example.replace(' ', '')
    ex_list = []
    count = 0
    temp = 0
    for i in example:
        if i.isdigit():
            if count == len(example) - 1:
                ex_list.append(example[temp:])
            count += 1
        else:
            ex_list.append(example[temp:count])
            ex_list.append(example[count])
            temp = count + 1
            count += 1

    while len(ex_list) > 1:
        count = 1
        res = 0
        if ('/' in ex_list) or ('*' in ex_list):
            while ('/' in ex_list) or ('*' in ex_list):
                if ex_list[count] == '*':
                    res = float(list(ex_list)[count-1]) * float(list(ex_list)[count+1])
                    ex_list.insert(count - 1, res)
                    del ex_list[count:count + 3]
                    count = -1
                elif ex_list[count] == '/':
                    res = float(list(ex_list)[count-1]) / float(list(ex_list)[count+1])
                    ex_list.insert(count - 1, res)
                    del ex_list[count:count + 3]
                    count = -1
                count += 2

        elif ex_list[count] == '+':
            res = float(list(ex_list)[count-1]) + float(list(ex_list)[count+1])
            ex_list.insert(count - 1, res)
            del ex_list[count:count + 3]
        elif ex_list[count] == '-':
            res = float(list(ex_list)[count-1]) - float(list(ex_list)[count+1])
            ex_list.insert(count - 1, res)
            del ex_list[count:count + 3]

    return ex_list