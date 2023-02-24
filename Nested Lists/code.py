if __name__ == '__main__':
    students = []
    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append(score)
        students.append([name, score])

    grades = set(grades)

    grades.remove(min(grades))

    names = []

    for i in range(len(students)):
        if students[i][1] == min(grades):
            names.append(students[i][0])
    names.sort()
    for i in range(len(names)):
        print(names[i])
