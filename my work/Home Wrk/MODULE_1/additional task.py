grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
a_0 = sum(grades[0]) / len(grades[0])
a_1 = sum(grades[1]) / len(grades[1])
a_2 = sum(grades[2]) / len(grades[2])
a_3 = sum(grades[3]) / len(grades[3])
a_4 = sum(grades[4]) / len(grades[4])
average_grade = {
    students[0]: a_0,
    students[1]: a_1,
    students[2]: a_2,
    students[3]: a_3,
    students[4]: a_4
}
print(average_grade)
