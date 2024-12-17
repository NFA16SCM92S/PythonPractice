class Student:
# creating a student data type
# add attributes for student in the constructor- initialization method
# We can create our own data type using class.
# constructors, destructors,
# write a program for student
    def __init__(self, name, major, class_year, gpa, is_on_probation):
        self.name = name
        # The name of the Student's object is going
        # to be equal to the name we passed as parameter
        # self.name and others are attributes of the object, which is different from the na,e
        #major, etc passed in the __init__ function
        self.major = major
        self.class_year = class_year
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

