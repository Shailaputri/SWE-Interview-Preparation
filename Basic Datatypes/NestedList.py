if __name__ == '__main__':
    student_name = []
    student_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_name.append(name)
        student_score.append(score)
    i = 0
    python_students = []
    while i < len(student_name):
        python_students.append([student_name[i],student_score[i]])
        i += 1
    python_students.sort(key = lambda x:x[1])
    max_python_students = max(python_students, key = lambda y:y[1])
    sub_list = [ele for ele in python_students if ele[1]<max_python_students[1]]
    new_list = []
    for ele in sub_list:
        if ele[1]==sub_list[-1][1]:
            new_list.append(ele[0])
    new_list.sort()
    for ele in new_list:
        print(ele)
