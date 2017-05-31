class Student:
    def __init__(self):
        self.name, final, union, leader, west, paper = raw_input().strip().split()
        final = int(final)
        union = int(union)
        leader = leader == 'Y'
        west = west == 'Y'
        paper = int(paper)
        money = 0
        if final > 80 and paper >= 1: money += 8000
        if final > 85 and union > 80: money += 4000
        if final > 90: money += 2000
        if final > 85 and west: money += 1000
        if union > 80 and leader: money += 850
        self.money = money


students = []
for i in xrange(int(raw_input())):
    students.append(Student())
students = sorted(students, key=lambda s: -s.money)
print students[0].name
print students[0].money
print sum(x.money for x in students)
