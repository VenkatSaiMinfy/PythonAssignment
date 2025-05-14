from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "grades"])

def top_student(students):
    return max(students, key=lambda s: sum(s.grades) / len(s.grades))

n = int(input("n: "))
students = []

for _ in range(n):
    name = input("name: ")
    age = int(input("age: "))
    grades = tuple(map(int, input("grades: ").split()))
    students.append(Student(name, age, grades))

print(top_student(students))
