from student import Student
#create objects which is instance of Class/data type Student
student1 = Student("Jim" , "MS of CS", 2024, 3.1, False)
student2 = Student("Mark", "MBA", 2023, 3.7, True)
# call the attributes of the class using object
print(student1.name)
print(student2.is_on_probation)
print(student1.on_honor_roll())
print(student2.on_honor_roll())