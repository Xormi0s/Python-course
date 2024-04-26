class OnlineCourse:
    def __init__(self, course, teacher):
        self.course = course
        self.teacher = teacher
        self.students = []
        
    def enroll_students(self, student):
        self.students.append(student)
        print(f"{student.name} has been enrolled in the {self.course} course.")
        
    def course_details(self):
        print(f"Course: {self.course}")
        print(f"Teacher: {self.teacher}")
        print("Enrolled students: ")
        for student in self.students:
            print(student.name)
        
    def completed_course(self, name):
        for student in self.students:
            if student.name in name:
                self.students.remove(student)
                print(f"{name} has completed the course!")
        print(f"{name} is not enrolled in this course!")
            
    def avg_grade(self, student):
        total = sum(student.grades)
        average = total/len(student.grades)
        print(f"The average grade is: {round(average)}")
        
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        
course_input = input("Enter a course: ").lower()
name = input("Enter a teacher: ").lower()

course = OnlineCourse(course_input, name)

num_students = int(input("Enter the number of students: "))

for  _ in range(num_students):
    student_name = input("Enter a student name: ").lower()
    grades = []
    for _ in range(3):
        grade = int(input("Enter a grade: "))
        grades.append(grade)
    student = Student(student_name, grades)
    course.enroll_students(student)
    course.avg_grade(student)
    
course.course_details()
        
