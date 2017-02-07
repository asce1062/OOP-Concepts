# real-world problem modeled using OOP
# Depicts inheritance, encapsulation, polymorphism and the other OOP concepts.

class Person:
    def __init__(self, name, surname, id_number, student_type):
        self.name = name
        self.surname = surname
        self.id_number = id_number


class Student(Person):
    UNDERGRADUATE, POSTGRADUATE = range(2)

    def __init__(self, student_type, *args, **kwargs):
        self.student_type = student_type
        self.classes = []
        super(Student, self).__init__(*args, **kwargs)

    def enrol(self, course):
        self.classes.append(course)

    def courses_taught(self):
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)

    def menu(self, name):
        print("Welcome ",self.name, "! Kindly select an option:")
        print ("""1: Enroll
                  2: Courses taught
                  3: Lecturer assigned""")
        option = input("Option: ")
        if option == "1":
            return enrol()
        elif option == "2":
            return courses_taught()
        elif option == "3":
            return assign_teaching()
