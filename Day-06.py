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

Student1 = Student("Sandy", [95,97,86,98,92])
Student2 = Student("Kiana",[99,94,98,97,92])


import json
data = {"name":"Jahanvi",
        "age":16,
        "skills":["python","SQL"],
        "confident with":"python"}

with open("data.json","w") as f:
    json.dump(data,f)

with open("data.json","r") as f:
    loaded = json.load(f)
    print("name:",loaded["name"])
    print("age:" ,loaded["age"])
    print("skills:" ,loaded["skills"])
    print("confident with:",loaded["confident with"])


import csv
with open("students.csv","w" , newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name","average_grade"])
    writer.writerow([Student1.name,Student1.average_grade()])
    writer.writerow([Student2.name,Student2.average_grade()])


with open("students.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

