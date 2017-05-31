class Student(object):
    def __init__(self):
        line = raw_input().strip()
        self.name, self.number, self.gender = line.split()


def find(k, s):
    for i in xrange(len(s)):
        student = students[i]
        if k == student.name or k == student.number:
            return i
    return -1


students = []
for case in xrange(int(raw_input().strip())):
    students.append(Student())
for case in xrange(int(raw_input().strip())):
    a, b = raw_input().strip().split()
    ia, ib = find(a, students), find(b, students)
    print 'Y' if students[ia].gender != students[ib].gender else 'N'
