class Teacher:
    def __init__(self,name, index, subject,priority, score_info, score_subject):
        self.name = name
        self.subject = subject
        self.priority = priority
        self.index = index
        self.score = score_info * 2 + score_subject + priority
        if len(self.name) > 50:
            raise InvalidName
        if score_info < 0 or score_info > 10 or score_subject < 0 or score_subject > 10:
            raise InvalidScore

    def Admission(self):
        if self.score >= 18:
            return 'ADMITTED'
        else:
            return 'REJECTED'

    def __str__(self):
        return f'GV0{self.index} {self.name} {self.subject} {self.score} {self.Admission()}'
class InvalidName(Exception):
    pass
class InvalidScore(Exception):
    pass
Priority_score = {1:2.0, 2:1.5, 3:1.0, 4: 0.0}
Subject_list = {'A': 'MATH', 'B': 'PHYSICS', 'C': 'CHEMISTRY'}
n = int(input())
teachers = []
for i in range(n):
    name = f'{input()}'
    code = input().split()
    score_info = float(input())
    score_subject = float(input())
    index = i + 1
    subject = Subject_list.get(code[0][0])
    priority = Priority_score.get(int(code[0][1]))
    teacher = Teacher(name, index, subject, priority, score_info, score_subject)

    teachers.append(teacher)

teachers.sort(key=lambda teacher: teacher.score, reverse=True)
for teacher in teachers:
    print(teacher)
    print()