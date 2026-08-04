class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, grades):
        super().__init__(name)
        self.grades = grades

    def average_grade(self):

        return sum(self.grades) / len(self.grades)

    pass

    def add_grade(self, grade):
        self.grades.append(grade)

    pass

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def teach(self):
        return f"{self.name} teaches {self.subject}"
Teacher1 = Teacher("Rossy","Maths")
Teacher2 = Teacher("kang tae-moor","Physics")
Student1 = Student("Sandy", [95,97,86,98,92])
Student2 = Student("Kiana",[99,94,98,97,92])
print(Teacher1.teach())
print(Student1.name,Student1.grades,Student1.average_grade())
print(Teacher2.teach())
print(Student2.name,Student2.grades,Student2.average_grade())

