'''
This program is to create, traverse, retrieve elements from a nested list.
Nested list is L[[],[],[]]. So L[0][0] gives the 1st element at L[0].


Problem statement : Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''




student_name = []
student_score = []
for _ in range(int(input("How many entries?"))):
    name = input("Name:\t")
    score = float(input("Score:\t"))
    student_name.append(name)
    student_score.append(score)
i = 0
python_students = []
while i < len(student_name):
    python_students.append([student_name[i],student_score[i]])
    i += 1
python_students.sort(key = lambda x:x[1])
print(python_students)
min_python_students = min(python_students, key = lambda y:y[1])
sub_list = [ele for ele in python_students if ele[1]>min_python_students[1]]
new_list = []
for ele in sub_list:
    if ele[1]==sub_list[0][1]:
        new_list.append(ele[0])
new_list.sort()
for ele in new_list:
    print(ele)