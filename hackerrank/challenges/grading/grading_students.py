# grading students
# https://www.hackerrank.com/challenges/grading/problem

def grading_students(grades: list[int]) -> list[int]:
    for i in range(len(grades)):
        if grades[i] > 37 and grades[i] % 5 > 2:
            grades[i] = (grades[i] // 5 + 1) * 5

    return grades
