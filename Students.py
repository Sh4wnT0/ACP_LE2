class Student:
    # Initializing the information we needed.
    def __init__(self, id_name, email, grades=None, courses=None):
        self.id_name = id_name if id_name is not None else {}
        self.email = email
        self.grades = grades if grades is not None else {}
        self.courses = courses if courses is not None else []

    # Method to understand the information when displayed.
    def __str__(self):
        return f"Student ID: {self.id_name.get('id', '')}, Name: {self.id_name.get('name', '')}, Email: {self.email}, Grades: {self.grades}, Courses: {self.courses}"
        pass
    
    #Getting the GPA uising the given grades.
    def gpa(self):
        name = self.id_name.get("name", "")
        if not self.grades:
            print("No recorded grades.")
            return None
        total = sum(self.grades.values())
        total_values = len(self.grades)
        average = total / total_values
        print("This is the GPA of ", name, average)

# Creating a class to handle multiple student records.
class StudentRecord:
    # Empty list  wherein we are storing the student records.
    def __init__(self):
        self.records = []

    def __str__(self):
     return "\n".join(str(student) for student in self.records)

    # Add record method using the append function.
    def add_record(self, student):
        self.records.append(student)
        print("Record added successfully.")

    # Updating Info using student id_name("id")
    def update_student(self, student_id, email = None, grades = None, courses = None ):
        for student in self.records:
            if student.id_name.get("id") == student_id:
                if email is not None:
                    student.email = email
                if grades is not None:
                    student.grades = grades
                if courses is not None:
                    student.courses = courses
                print(f"Student Info by the ID {student_id} updated successfully.")
                return
        print("No student found with the given ID", student_id)
    
    # Getting Info using partial name search using .lower() and "in" functions.
    def gs_by_name(self, student_name):
        print("Searching records for the name: ", student_name)
        for student in self.records:
            name = student.id_name.get("name", "").lower() 
            if student_name.lower() in name:
                return student
        print("No students have the name: ", student_name)
        return None
    
    # Getting Info using id_name.get("id").
    def gs_by_id(self, student_id):
        print("Searching records for the ID: ", student_id)
        for student in self.records:
            if student.id_name.get("id") == student_id:
                return student
        print("No students have the Id:", student_id)
        return None
    
    # Deleting record using the remove function.
    def delete_student(self, student_id):
        for student in self.records:
            if student.id_name.get("id") == student_id:
                self.records.remove(student)
                print(f"Student records with the ID:{student_id} deleted succesfully")
                return
        print("Unable to find a student with ID:", student_id)

    #Enrolling to a course and ensuring no duplicate using the "not in" function.
    def add_course(self, student_id, course):
        for student in self.records:
            if student.id_name.get("id") == student_id:
                if course not in student.courses:  
                    student.courses.append(course)
                    print(f"Student with the ID:{student_id} successfully enrolled in {course}")
                else:
                    print(f"Student ID {student_id} is already enrolled in '{course}'.")
                return
        print("Unable to find a student with ID:", student_id)
        return None

    

# Create StudentRecord manager to be able to call and display all the records easily.
record = StudentRecord()

# Add student infos
student1 = Student({"id": 1, "name": "Jinko"}, "jinko@example.com", {"math": 90}, ["math"])
student2 = Student({"id": 2, "name": "Kupa"}, "kupa@example.com", {"science": 85}, ["science"])

print("Calling the add_record method: ")
record.add_record(student1)
record.add_record(student2)

# Printing all records using the manager we created
print("\nAll Records:")
print(record)

# Update student info
print("\nUpdating Info for Student ID:1 ")
record.update_student(1, email="new@example.com", grades={"math": 75, "english": 80}, courses=["math", "english"])
print(record)

# Search by name
print("\nSearch by Name:")
get_by_name = record.gs_by_name("jin")
print(get_by_name)
print()
wrong_name = record.gs_by_name("JinkoBiloba")
print(f"{wrong_name}")

# Search by ID
print("\nSearch by ID:")
get_by_id = record.gs_by_id(2)
print(get_by_id)
print()
wrong_id = record.gs_by_id(36)
print(wrong_id)

# Enroll in a new course
print("\nEnroll in Course:")
record.add_course(2, "math")  # New course
record.add_course(2, "science")  # Duplicate
print(record)

# Delete a student
print("\nDelete Student:")
record.delete_student(1)
print(record)

# GPA method
print("\nGetting the student GPA:")
student2.gpa()
