class Student:
    id_name = []
    grades = {}
    course = []

    def __init__(self, id_name, email, grades=None, courses=None):
        self.id_name = id_name if id_name is not None else {}
        self.email = email
        self.grades = grades if grades is not None else {}
        self.courses = courses if courses is not None else []

    def __str__(self):
        return f"Student ID: {self.id_name.get('id', '')}, Name: {self.id_name.get('name', '')}, Email: {self.email}, Grades: {self.grades}, Courses: {self.courses}"
        pass

class StudentRecord:
    records = []

    def __init__(self):
        self.records = []

    def add_record(self, student):
        self.records.append(student)
        print("Record added successfully.")

student1 = Student({"id": 1, "name": "Jinko"}, "jinko@example.com", {"math": 90, "science": 85}, ["math", "science"])
print(student1)
student2 = Student({"id": 2, "name": "Kupal"}, "kupal@example.com", {"math": 80, "science": 90}, ["math", "science"])

student1 = StudentRecord()
student1.add_record(student1)
print(student1)
