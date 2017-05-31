import sys

n, m = map(int, sys.stdin.readline().strip().split())


class Student:
    def __init__(self, name, arr):
        self.name, self.arr = name, arr
        ac, time = 0, 0
        for s in self.arr:
            if '(' in s:
                a, b = s.split('(')
                time += m * int(b[:-1]) + int(a)
                ac += 1
            else:
                s = int(s)
                if s > 0:
                    ac += 1
                    time += s
        self.ac, self.time = ac, time


students = []
for line in sys.stdin.readlines():
    data = line.strip().split()
    students.append(Student(data[0].strip(), data[1:]))

students = sorted(students, key=lambda s: (-s.ac, s.time, s.name))
for student in students:
    print student.name.ljust(10) + ' %2d %4d' % (student.ac, student.time)
