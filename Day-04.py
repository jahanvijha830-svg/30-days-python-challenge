class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grade = grades

    def average_grade(self):

        return sum(self.grade) / len(self.grade)

    pass

    def add_grade(self, grade):
        self.grade.append(grade)

    pass
student1= Student("Ram", [90,91,99,95])
student1.add_grade(92)
student2 = Student("Kia", [93,92,91,60])
student2.add_grade(80)
print(student1.name, student1.grade,student1.average_grade())
print(student2.name, student2.grade,student2.average_grade())








