name = 'Tom'
subj = 'math'
grad = 5
student_subject = {'Tom': {'math': []}, 'Bob': {'fikk': []}}
student_subject[name][subj].append(grad)


print(student_subject)
