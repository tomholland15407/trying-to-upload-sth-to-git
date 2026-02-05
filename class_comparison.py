class Student:
    def __init__(self, name, ID, Grade):
        self.name = name
        self.ID = ID
        self.Grade = Grade
    def __str__(self):
        return f'Name: {self.name}\nID: {self.ID}\nGrade: {self.Grade}'
    def __lt__(self, other):
        return self.Grade < other.Grade
    def __gt__(self, other):
        return self.Grade > other.Grade
    def __eq__(self, other):
        return self.ID == other.ID
    def GradeType(self):
        if self.Grade >= 3.6:
            return 'Excellent'
        elif self.Grade >= 3.2:
            return 'Good'
        elif self.Grade >= 2.5:
            return 'Fair'
        else:
            return 'Poor'
s1 = Student('Nguyen Van An', 20201000, 3.75)
s2 = Student('Le Van Toan', 20202345, 2.80)
s3 = Student('Tran Thi Dung', 20201000, 3.12)
print(s1)
print(s2 < s1 and s3 < s1)
print(s1 == s3)
print(s1.GradeType())
print(s2.GradeType())