class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []
    
    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)
    
    def __str__(self):
        courses_list = ', '.join([course.name for course in self.courses]) or 'None'
        return f"\nStudent Information:\n- Name: {self.name}\n- ID: {self.student_id}\n- Age: {self.age}\n- Courses Enrolled: {courses_list}\n"

class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.courses = []
    
    def assign_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.assign_teacher(self)
    
    def __str__(self):
        courses_list = ', '.join([course.name for course in self.courses]) or 'None'
        return f"\nTeacher Information:\n- Name: {self.name}\n- ID: {self.teacher_id}\n- Age: {self.age}\n- Courses Assigned: {courses_list}\n"

class Course:
    def __init__(self, name, course_code):
        self.name = name
        self.course_code = course_code
        self.teacher = None
        self.students = []
    
    def assign_teacher(self, teacher):
        self.teacher = teacher
    
    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
    
    def __str__(self):
        teacher_name = self.teacher.name if self.teacher else 'None'
        students_list = ', '.join([student.name for student in self.students]) or 'None'
        return f"\nCourse Information:\n- Name: {self.name}\n- Code: {self.course_code}\n- Teacher: {teacher_name}\n- Enrolled Students: {students_list}\n"

class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.courses = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    
    def add_course(self, course):
        self.courses.append(course)
    
    def __str__(self):
        return (f"\nSchool Information:\n- Name: {self.name}\n"
                f"- Total Students: {len(self.students)}\n"
                f"- Total Teachers: {len(self.teachers)}\n"
                f"- Total Courses: {len(self.courses)}\n")

school = School("Greenwood High")

student1 = Student("Krunal", 15, 101)
student2 = Student("Aditya", 16, 102)

teacher1 = Teacher("Jeet Jha", 40, 201)

course1 = Course("Pyhton", "Python Full Stack")

teacher1.assign_course(course1)

student1.enroll(course1)
student2.enroll(course1)

school.add_student(student1)
school.add_student(student2)
school.add_teacher(teacher1)
school.add_course(course1)

print(school)
print(student1)
print(student2)
print(teacher1)
print(course1)
