if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        list = []
        name = input()
        list.append(name)
        score = float(input())
        list.append(score)
        students.append(list)
    lowest = students[0][1]
    position = 0
    for i in range(len(students)):
        if lowest >= students[i][1]:
            lowest = students[i][1]
    temp = students[0][1]
    second = 0
    slist = []
    for i in range(len(students)):
        if not(lowest == students[i][1]):
            temp = students[i][1]
    for i in range(len(students)):
        if not(lowest == students[i][1]):
            if temp > students[i][1]:
                temp = students[i][1]
    for i in range(len(students)):
        if not(lowest == students[i][1]):
            if temp == students[i][1]:
                slist.append(students[i][0])
    slist.sort()
    for i in slist:
        print(i)
